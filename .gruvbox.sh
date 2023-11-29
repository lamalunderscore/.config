###change theme to gruvbox###

#change nvim theme


#change rofi theme
echo change rofi theme
cp ~/.config/rofi/confbase.rasi ~/.config/rofi/config.rasi
echo "@theme \"gruvbox\"" >> ~/.config/rofi/config.rasi
echo done
echo



#change polybar theme
echo change polybar theme
cp ~/.config/polybar/confbase ~/.config/polybar/config
echo "include-file = ~/.config/polybar/gruvbox.ini" >> ~/.config/polybar/config
cp ~/.config/polybar/scripts/gruvbox ~/.config/polybar/scripts/bluetooth.sh
echo done
echo


#change zathura theme

#change gtk theme
echo change gtk theme
cp ~/.config/gtk-3.0/confbase.ini ~/.config/gtk-3.0/settings.ini
echo "gtk-theme-name=Gruvbox-Material-Dark" >> ~/.config/gtk-3.0/settings.ini
echo "gtk-icon-theme-name=Gruvbox-Material-Dark" >> ~/.config/gtk-3.0/settings.ini
echo done
echo


#change fish theme
echo change fish theme
cp ~/.config/fish/themes/gruvbox.fish ~/.config/fish/conf.d/theme.fish
echo done
echo

#change kitty theme
echo change kitty theme
cp ~/.config/kitty/confbase.conf ~/.config/kitty/kitty.conf
echo "include gruvbox_dark.conf" >> ~/.config/kitty/kitty.conf
echo done
echo

#change i3 theme
echo change i3 theme
cp ~/.config/i3/confbase ~/.config/i3/config
echo "include gruvboxtheme" >> ~/.config/i3/config
echo done
echo

#change spotify theme
echo change spotify theme
spicetify config current_theme Onepunch
spicetify config color_scheme dark
spicetify update
echo done
echo
