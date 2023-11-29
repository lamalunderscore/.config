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
alias gccc="gcc -std=c99 -Wall -pedantic -g"
alias ssh="kitty +kitten ssh"

#wallpaper shortcuts
alias bg="nitrogen --random --set-auto /media/wallpapers/random"
alias bgb="nitrogen --set-tiled /media/wallpapers/random/tiled.png"
alias bgw="nitrogen --set-tiled /media/wallpapers/random/tiled_inverse.png"
alias bgm="nitrogen --set-auto /media/wallpapers/random/manindoor_cropped.jpg"
alias bga="nitrogen --set-auto /media/wallpapers/random/astronaut_cropped.jpg"
alias bgt="nitrogen --set-auto /media/wallpapers/random/treealone_cropped.jpg"
alias bgto="nitrogen --set-auto /media/wallpapers/random/tokyo_cropped.jpg"

#directory shortcuts
alias imp="cd ~/Desktop/uni/impprog/"
alias ads="cd ~/Desktop/uni/ads"


#config shortcuts
alias awesomec="nvim ~/.config/awesome/rc.lua"
alias fishc="nvim ~/.config/fish/confbase.fish"
alias kittyc="nvim ~/.config/kitty/confbase.conf"
alias rofic="nvim ~/.config/rofi/config.rasi"
alias i3c="nvim ~/.config/i3/confbase"
alias picomc="nvim ~/.config/picom/picom.conf"
alias polybarc="cd ~/.config/polybar/"
alias spicetifyc="nvim ~/.config/spicetify/config-xpui.ini"
alias nvc="cd ~/.config/nvim/"

#document shortcuts
alias todo="nvim ~/.todo"


#theme shortcuts
alias dracula="bash ~/.config/.dracula.sh"
alias gruvbox="bash ~/.config/.gruvbox.sh"

