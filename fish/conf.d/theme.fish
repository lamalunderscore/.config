#bobthefish
set -g theme_color_scheme gruvbox

# Dracula Color Palette
set -l foreground ebdbb2
set -l selection 7c6f64
set -l comment 458588
set -l red cc241d
set -l orange d65d0e
set -l yellow d79921
set -l green 98971a
set -l purple b16286
set -l cyan 689d6a
set -l pink d3869b

# Syntax Highlighting Colors
set -g fish_color_normal $foreground
set -g fish_color_command $green
set -g fish_color_keyword $orange
set -g fish_color_quote $yellow
set -g fish_color_redirection $orange
set -g fish_color_end $pink
set -g fish_color_error $red
set -g fish_color_param $normal
set -g fish_color_comment $comment
set -g fish_color_selection --background=$selection
set -g fish_color_search_match --background=$selection
set -g fish_color_operator $green
set -g fish_color_escape $orange
set -g fish_color_autosuggestion $orange

# Completion Pager Colors
set -g fish_pager_color_progress $comment
set -g fish_pager_color_prefix $cyan
set -g fish_pager_color_completion $orange
set -g fish_pager_color_description $comment
