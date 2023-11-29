function fish_greeting
#  cowsay "'sup" | lolcat  -F 5.0 -p 10.0
end

if status is-interactive
    # Commands to run in interactive sessions can go here
end


#program shortcuts
alias pac="sudo pacman -S"
alias pacm="sudo pacman"
alias nv="nvim"
alias gccc="gcc -std=c99 -Wall -pedantic"

#wallpaper shortcuts
alias bg="nitrogen --random --set-auto /media/wallpapers/random"
alias bgb="nitrogen --set-tiled /media/wallpapers/random/tiled.png"
alias bgw="nitrogen --set-tiled /media/wallpapers/random/tiled_inverse.png"
alias bgm="nitrogen --set-auto /media/wallpapers/random/manindoor_cropped.jpg"
alias bga="nitrogen --set-auto /media/wallpapers/random/astronaut_cropped.jpg"
alias bgt="nitrogen --set-auto /media/wallpapers/random/treealone_cropped.jpg"

#directory shortcuts
alias imp="cd ~/Desktop/uni/impprog/"


#config shortcuts
alias awesomec="nvim ~/.config/awesome/rc.lua"
alias fishc="nvim ~/.config/fish/config.fish"
alias kittyc="nvim ~/.config/kitty/confbase.conf"
alias rofic="nvim ~/.config/rofi/config.rasi"
alias i3c="nvim ~/.config/i3/confbase"
alias picomc="nvim ~/.config/picom/picom.conf"
alias polybarc="cd ~/.config/polybar/"
alias spicetifyc="nvim ~/.config/spicetify/config-xpui.ini"
alias nvc="nvim ~/.config/nvim/init.vim"

#document shortcuts
alias todo="nvim ~/.todo"


#theme shortcuts
alias dracula="bash ~/.dracula.sh"
alias gruvbox="bash ~/.gruvbox.sh"


#bobthefish
set -g theme_display_git yes
set -g theme_display_git_dirty no
set -g theme_display_git_untracked yes
set -g theme_display_git_ahead_verbose yes
set -g theme_display_git_dirty_verbose yes
set -g theme_display_git_stashed_verbose yes
set -g theme_display_git_default_branch yes
set -g theme_display_git_master_branch yes
set -g theme_git_default_branches master main
set -g theme_git_worktree_support no
set -g theme_use_abbreviated_branch_name no
set -g theme_display_vagrant yes
set -g theme_display_docker_machine no
set -g theme_display_k8s_context yes
set -g theme_display_hg yes
set -g theme_display_virtualenv no
set -g theme_display_nix no
set -g theme_display_ruby no
set -g theme_display_node yes
set -g theme_display_user ssh
set -g theme_display_hostname ssh
set -g theme_display_vi no
set -g theme_display_date no
set -g theme_display_cmd_duration yes
set -g theme_title_display_process yes
set -g theme_title_display_path no
set -g theme_title_display_user yes
set -g theme_title_use_abbreviated_path no
set -g theme_date_format "+%a %H:%M"
set -g theme_date_timezone America/Los_Angeles
set -g theme_avoid_ambiguous_glyphs yes
set -g theme_powerline_fonts no
set -g theme_nerd_fonts yes
set -g theme_show_exit_status yes
set -g theme_display_jobs_verbose yes
set -g default_user your_normal_user
set -g theme_color_scheme dark
set -g fish_prompt_pwd_dir_length 0
set -g theme_project_dir_length 1
set -g theme_newline_cursor yes
set -g theme_newline_prompt '$ '
