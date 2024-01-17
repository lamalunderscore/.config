# name: bobthefish
#
# bobthefish is a Powerline-style, Git-aware fish theme optimized for awesome.
#
# You will need a Powerline-patched font for this to work:
#
#     https://powerline.readthedocs.org/en/master/installation.html#patched-fonts
#
# I recommend picking one of these:
#
#     https://github.com/Lokaltog/powerline-fonts
#
# For more advanced awesome, install a nerd fonts patched font (and be sure to
# enable nerd fonts support with `set -g theme_nerd_fonts yes`):
#
#     https://github.com/ryanoasis/nerd-fonts
#



# ==============================
# Helper methods
# ==============================

function __bobthefish_basename -d 'basically basename, but faster'
    string replace -r '^.*/' '' -- $argv
end

function __bobthefish_dirname -d 'basically dirname, but faster'
    string replace -r '/[^/]+/?$' '' -- $argv
end

function __bobthefish_pwd -d 'Get a normalized $PWD'
    # The pwd builtin accepts `-P` on at least Fish 3.x, but fall back to $PWD if that doesn't work
    builtin pwd -P 2>/dev/null
    or echo $PWD
end

# Note that for fish < 3.0 this falls back to unescaped, rather than trying to do something clever /shrug
# After we drop support for older fishies, we can inline this without the fallback.
function __bobthefish_escape_regex -a str -d 'A backwards-compatible `string escape --style=regex` implementation'
    string escape --style=regex "$str" 2>/dev/null
    or echo "$str"
end

function __bobthefish_git_branch -S -d 'Get the current git branch (or commitish)'
    set -l branch (command git symbolic-ref HEAD 2>/dev/null | string replace -r '^refs/heads/' '')
    and begin
        [ -n "$theme_git_default_branches" ]
        or set -l theme_git_default_branches master main

        #[ "$theme_display_git_master_branch" != 'yes' -a "$theme_display_git_default_branch" != 'yes' ]
        #and contains $branch $theme_git_default_branches
        #and echo $branch_glyph
        #and return

        # truncate the middle of the branch name, but only if it's 25+ characters
        set -l truncname $branch
        [ "$theme_use_abbreviated_branch_name" = 'yes' ]
        and set truncname (string replace -r '^(.{17}).{3,}(.{5})$' "\$1…\$2" $branch)

        echo $branch_glyph $truncname
        and return
    end

    set -l tag (command git describe --tags --exact-match 2>/dev/null)
    and echo "$tag_glyph $tag"
    and return

    set -l branch (command git show-ref --head -s --abbrev | head -n1 2>/dev/null)
    echo "$detached_glyph $branch"
end

function __bobthefish_hg_branch -S -d 'Get the current hg branch'
    set -l branch (command hg branch 2>/dev/null)
    set -l book (command hg book | command grep \* | cut -d\  -f3)
    echo "$branch_glyph $branch @ $book"
end

function __bobthefish_pretty_parent -S -a child_dir -d 'Print a parent directory, shortened to fit the prompt'
    set -q fish_prompt_pwd_dir_length
    or set -l fish_prompt_pwd_dir_length 1

    # Replace $HOME with ~
    set -l real_home ~
    set -l parent_dir (string replace -r '^'(__bobthefish_escape_regex "$real_home")'($|/)' '~$1' (__bobthefish_dirname $child_dir))

    # Must check whether `$parent_dir = /` if using native dirname
    if [ -z "$parent_dir" ]
        echo -n /
        return
    end

    if [ $fish_prompt_pwd_dir_length -eq 0 ]
        echo -n "$parent_dir/"
        return
    end

    string replace -ar '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' "$parent_dir/"
end

function __bobthefish_ignore_vcs_dir -a real_pwd -d 'Check whether the current directory should be ignored as a VCS segment'
    for p in $theme_vcs_ignore_paths
        set ignore_path (realpath $p 2>/dev/null)
        switch $real_pwd/
            case $ignore_path/\*
                echo 1
                return
        end
    end
end

function __bobthefish_git_project_dir -S -a real_pwd -d 'Print the current git project base directory'
    [ "$theme_display_git" = 'no' ]
    and return

    set -q theme_vcs_ignore_paths
    and [ (__bobthefish_ignore_vcs_dir $real_pwd) ]
    and return

    if [ "$theme_git_worktree_support" != 'yes' ]
        set -l git_toplevel (command git rev-parse --show-toplevel 2>/dev/null)

        [ -z "$git_toplevel" ]
        and return

        # If there are no symlinks, just use git toplevel
        switch $real_pwd/
            case $git_toplevel/\*
                echo $git_toplevel
                return
        end

        # Otherwise, we need to find the equivalent directory in the $PWD
        set -l d $real_pwd
        while not [ -z "$d" ]
            if [ (realpath "$d") = "$git_toplevel" ]
                echo $d
                return
            end

            [ "$d" = '/' ]
            and return

            set d (__bobthefish_dirname $d)
        end
        return
    end

    set -l git_dir (command git rev-parse --git-dir 2>/dev/null)
    or return

    pushd $git_dir
    set git_dir (__bobthefish_pwd)
    popd

    switch $real_pwd/
        case $git_dir/\*
            # Nothing works quite right if we're inside the git dir
            # TODO: fix the underlying issues then re-enable the stuff below

            # # if we're inside the git dir, sweet. just return that.
            # set -l toplevel (command git rev-parse --show-toplevel 2>/dev/null)
            # if [ "$toplevel" ]
            #   switch $git_dir/
            #     case $toplevel/\*
            #       echo $git_dir
            #   end
            # end
            return
    end

    set -l project_dir (__bobthefish_dirname $git_dir)

    switch $real_pwd/
        case $project_dir/\*
            echo $project_dir
            return
    end

    set project_dir (command git rev-parse --show-toplevel 2>/dev/null)
    switch $real_pwd/
        case $project_dir/\*
            echo $project_dir
    end
end

function __bobthefish_hg_project_dir -S -a real_pwd -d 'Print the current hg project base directory'
    [ "$theme_display_hg" = 'yes' ]
    or return

    set -q theme_vcs_ignore_paths
    and [ (__bobthefish_ignore_vcs_dir $real_pwd) ]
    and return

    set -l d $real_pwd
    while not [ -z "$d" ]
        if [ -e $d/.hg ]
            command hg root --cwd "$d" 2>/dev/null
            return
        end

        [ "$d" = '/' ]
        and return

        set d (__bobthefish_dirname $d)
    end
end

function __bobthefish_project_pwd -S -a project_root_dir -a real_pwd -d 'Print the working directory relative to project root'
    set -q theme_project_dir_length
    or set -l theme_project_dir_length 0

    set -l project_dir (string replace -r '^'(__bobthefish_escape_regex "$project_root_dir")'($|/)' '' $real_pwd)

    if [ $theme_project_dir_length -eq 0 ]
        echo -n $project_dir
        return
    end

    string replace -ar '(\.?[^/]{'"$theme_project_dir_length"'})[^/]*/' '$1/' $project_dir
end

function __bobthefish_git_ahead -S -d 'Print the ahead/behind state for the current branch'
    if [ "$theme_display_git_ahead_verbose" = 'yes' ]
        __bobthefish_git_ahead_verbose
        return
    end

    set -l ahead 0
    set -l behind 0
    for line in (command git rev-list --left-right '@{upstream}...HEAD' 2>/dev/null)
        switch "$line"
            case '>*'
                if [ $behind -eq 1 ]
                    echo '±'
                    return
                end
                set ahead 1
            case '<*'
                if [ $ahead -eq 1 ]
                    echo "$git_plus_minus_glyph"
                    return
                end
                set behind 1
        end
    end

    if [ $ahead -eq 1 ]
        echo "$git_plus_glyph"
    else if [ $behind -eq 1 ]
        echo "$git_minus_glyph"
    end
end

function __bobthefish_git_ahead_verbose -S -d 'Print a more verbose ahead/behind state for the current branch'
    set -l commits (command git rev-list --left-right '@{upstream}...HEAD' 2>/dev/null)
    or return

    set -l behind (count (for arg in $commits; echo $arg; end | command grep '^<'))
    set -l ahead (count (for arg in $commits; echo $arg; end | command grep -v '^<'))

    switch "$ahead $behind"
        case '' # no upstream
        case '0 0' # equal to upstream
            return
        case '* 0' # ahead of upstream
            echo "$git_ahead_glyph$ahead"
        case '0 *' # behind upstream
            echo "$git_behind_glyph$behind"
        case '*' # diverged from upstream
            echo "$git_ahead_glyph$ahead$git_behind_glyph$behind"
    end
end

function __bobthefish_git_dirty_verbose -S -d 'Print a more verbose dirty state for the current working tree'
    set -l changes (command git diff --numstat | awk '{ added += $1; removed += $2 } END { print "+" added "/-" removed }')
    or return

    echo "$changes " | string replace -r '(\+0/(-0)?|/-0)' ''
end

function __bobthefish_git_stashed -S -d 'Print the stashed state for the current branch'
    if [ "$theme_display_git_stashed_verbose" = 'yes' ]
        set -l stashed (command git rev-list --walk-reflogs --count refs/stash 2>/dev/null)
        or return

        echo -n "$git_stashed_glyph$stashed"
    else
        command git rev-parse --verify --quiet refs/stash >/dev/null
        and echo -n "$git_stashed_glyph"
    end
end


# ==============================
# Segment functions
# ==============================

function __bobthefish_start_segment -S -d 'Start a prompt segment'
    set -l bg $argv[1]
    set -e argv[1]
    set -l fg $argv[1]
    set -e argv[1]

    set_color normal # clear out anything bold or underline...
    set_color -b $bg $fg $argv

    switch "$__bobthefish_current_bg"
        case ''
            # If there's no background, just start one
            echo -n ' '
        case "$bg"
            # If the background is already the same color, draw a separator
            echo -ns $right_arrow_glyph ' '
        case '*'
            # otherwise, draw the end of the previous segment and the start of the next
            set_color $__bobthefish_current_bg
            echo -ns $right_black_arrow_glyph ' '
            set_color $fg $argv
    end

    set __bobthefish_current_bg $bg
end

function __bobthefish_path_segment -S -a segment_dir -d 'Display a shortened form of a directory'
    set -l segment_color $color_path
    set -l segment_basename_color $color_path

    if not [ -w "$segment_dir" ]
        set segment_color $color_path_nowrite
        set segment_basename_color $color_path_nowrite_basename
    end

    __bobthefish_start_segment $segment_color

    set -l directory
    set -l parent

    switch "$segment_dir"
        case /
            set directory '/'
        case "$HOME"
            set directory '~'
        case '*'
            set parent (__bobthefish_pretty_parent "$segment_dir")
            set directory (__bobthefish_basename "$segment_dir")
    end

    echo -n $parent
    set_color -b $segment_basename_color
    echo -ns $directory ' '
end

function __bobthefish_finish_segments -S -d 'Close open prompt segments'
    if [ -n "$__bobthefish_current_bg" ]
        set_color normal
        set_color $__bobthefish_current_bg
        echo -ns $right_black_arrow_glyph ' '
    end

    if [ "$theme_newline_cursor" = 'yes' ]
        echo -ens "\n"
        set_color $fish_color_autosuggestion

        if set -q theme_newline_prompt
            echo -ens "$theme_newline_prompt"
        else if [ "$theme_powerline_fonts" = 'no' -a "$theme_nerd_fonts" != 'yes' ]
            echo -ns '> '
        else
            echo -ns "$right_arrow_glyph "
        end
    else if [ "$theme_newline_cursor" = 'clean' ]
        echo -ens "\n"
    end

    set_color normal
    set __bobthefish_current_bg
end

# ==============================
# VCS segments
# ==============================

function __bobthefish_prompt_hg -S -a hg_root_dir -a real_pwd -d 'Display the actual hg state'
    set -l dirty (command hg stat; or echo -n '*')

    set -l flags "$dirty"
    [ "$flags" ]
    and set flags ''

    set -l flag_colors $color_repo
    if [ "$dirty" ]
        set flag_colors $color_repo_dirty
    end

    __bobthefish_path_segment $hg_root_dir

    __bobthefish_start_segment $flag_colors
    echo -ns $hg_glyph ' '

    __bobthefish_start_segment $flag_colors
    echo -ns (__bobthefish_hg_branch) $flags ' '
    set_color normal

    set -l project_pwd (__bobthefish_project_pwd $hg_root_dir $real_pwd)
    if [ "$project_pwd" ]
        if [ -w "$real_pwd" ]
            __bobthefish_start_segment $color_path
        else
            __bobthefish_start_segment $color_path_nowrite
        end

        echo -ns $project_pwd ' '
    end
end

function __bobthefish_prompt_git -S -a git_root_dir -a real_pwd -d 'Display the actual git state'
    

    set -l dirty ''
    if [ "$theme_display_git_dirty" != 'no' ]
        set -l show_dirty (command git config --bool bash.showDirtyState 2>/dev/null)
        if [ "$show_dirty" != 'false' ]
            set dirty (command git diff --no-ext-diff --quiet --exit-code 2>/dev/null; or echo -n "$git_dirty_glyph")
            if [ "$dirty" -a "$theme_display_git_dirty_verbose" = 'yes' ]
                set dirty "$dirty"(__bobthefish_git_dirty_verbose)
            end
        end
    end

    set -l staged (command git diff --cached --no-ext-diff --quiet --exit-code 2>/dev/null; or echo -n "$git_staged_glyph")
    set -l stashed (__bobthefish_git_stashed)
    set -l ahead (__bobthefish_git_ahead)

    set -l new ''
    if [ "$theme_display_git_untracked" != 'no' ]
        set -l show_untracked (command git config --bool bash.showUntrackedFiles 2>/dev/null)
        if [ "$show_untracked" != 'false' ]
            set new (command git ls-files --other --exclude-standard --directory --no-empty-directory 2>/dev/null)
            if [ "$new" ]
                set new "$git_untracked_glyph"
            end
        end
    end

    set -l flags "$dirty$staged$stashed$ahead$new"

    [ "$flags" ]
    and set flags " $flags"

    set -l flag_colors $color_repo
    if [ "$dirty" ]
        set flag_colors $color_repo_dirty
    else if [ "$staged" ]
        set flag_colors $color_repo_staged
    end

    #__bobthefish_path_segment $git_root_dir

    __bobthefish_start_segment $flag_colors


    echo -ns (__bobthefish_git_branch) $flags ' '
    set_color normal

    #if [ "$theme_git_worktree_support" != 'yes' ]
    #    set -l project_pwd (__bobthefish_project_pwd $git_root_dir $real_pwd)
    #    if [ "$project_pwd" ]
    #        if [ -w "$real_pwd" ]
    #            __bobthefish_start_segment $color_path
    #        else
    #            __bobthefish_start_segment $color_path_nowrite
    #        end
    #
    #       echo -ns $project_pwd ' '
    #    end
    #    return
    #end


    __bobthefish_path_segment $git_root_dir


    #set -l project_pwd (command git rev-parse --show-prefix 2>/dev/null | string trim --right --chars=/)
    #set -l work_dir (command git rev-parse --show-toplevel 2>/dev/null)

    # only show work dir if it's a parent…
    #if [ "$work_dir" ]
    #    switch $real_pwd/
    #        case $work_dir/\*
    #            string match "$git_root_dir*" $work_dir >/dev/null
    #            and set work_dir (string sub -s (math 1 + (string length $git_root_dir)) $work_dir)
    #        case \*
    #            set -e work_dir
    #    end
    #end

    #if [ "$project_pwd" -o "$work_dir" ]
    #    set -l colors $color_path
    #    if not [ -w "$real_pwd" ]
    #        set colors $color_path_nowrite
    #    end

    #    __bobthefish_start_segment $colors

    #    # handle work_dir != project dir
    #    if [ "$work_dir" ]
    #        #set -l work_parent (__bobthefish_dirname $work_dir)
    #        #if [ "$work_parent" ]
    #        #    echo -n "$work_parent/"
    #        #end
            #set_color normal
            #set_color -b $color_repo_work_tree
            #echo -n (__bobthefish_basename $work_dir)

            #set_color normal
            #set_color -b $colors
            #[ "$project_pwd" ]
            #and echo -n '/'
    #    end

        #echo -ns $project_pwd ' '
    #else
        #set project_pwd $real_pwd

    #    string match "$git_root_dir*" $project_pwd >/dev/null
    #    and set project_pwd (string sub -s (math 1 + (string length $git_root_dir)) $project_pwd)

    #    set project_pwd (string trim --left --chars=/ -- $project_pwd)

    #    if [ "$project_pwd" ]
    #        set -l colors $color_path
    #        if not [ -w "$real_pwd" ]
    #            set colors $color_path_nowrite
    #        end

    #        __bobthefish_start_segment $colors

    #        echo -ns $project_pwd ' '
    #    end
    #end
    set_color normal
end

function __bobthefish_prompt_dir -S -a real_pwd -d 'Display a shortened form of the current directory'
    __bobthefish_path_segment "$real_pwd"
end


# ==============================
# Apply theme
# ==============================

function fish_right_prompt -d 'bobthefish, a fish theme optimized for awesome'
    __bobthefish_glyphs
    __bobthefish_colors $theme_color_scheme

    type -q bobthefish_colors
    and bobthefish_colors

    set -l real_pwd (__bobthefish_pwd)

    # VCS
    set -l git_root_dir (__bobthefish_git_project_dir $real_pwd)
    set -l hg_root_dir (__bobthefish_hg_project_dir $real_pwd)

    if [ "$git_root_dir" -a "$hg_root_dir" ]
        # only show the closest parent
        switch $git_root_dir
            case $hg_root_dir\*
                __bobthefish_prompt_git $git_root_dir $real_pwd
            case \*
                __bobthefish_prompt_hg $hg_root_dir $real_pwd
        end
    else if [ "$git_root_dir" ]
        __bobthefish_prompt_git $git_root_dir $real_pwd
    else if [ "$hg_root_dir" ]
        __bobthefish_prompt_hg $hg_root_dir $real_pwd
    else
      #  __bobthefish_prompt_dir $real_pwd
    end
    

    #__bobthefish_finish_segments
end
