return {
  -- Set colorscheme to use
  colorscheme = "gruvbox",

  -- vim.o.updatetime = 250,
  -- vim.cmd [[autocmd! CursorHold,CursorHoldI * lua vim.diagnostic.open_float(nil, {focus=false})]],

  -- Diagnostics configuration (for vim.diagnostics.config({...})) when diagnostics are on
  diagnostics = {
    virtual_text = true,
    underline = true,
  },

  -- heirline = {
  --   separators = {
  --     none = { "", "" },
  --     left = { "", "  " },
  --     right = { "  ", "" },
  --     center = { "  ", "  " },
  --     tab = { "", " " },
  --     breadcrumbs = "  ",
  --     path = "  ",
  --   },
  --   colors = {
  --     fg = StatusLine.fg,
  --     bg = StatusLine.bg,
  --     section_fg = StatusLine.fg,
  --     section_bg = StatusLine.bg,
  --     git_branch_fg = Conditional.fg,
  --     treesitter_fg = String.fg,
  --     scrollbar = TypeDef.fg,
  --     git_added = GitSignsAdd.fg,
  --     git_changed = GitSignsChange.fg,
  --     git_removed = GitSignsDelete.fg,
  --     diag_ERROR = DiagnosticError.fg,
  --     diag_WARN = DiagnosticWarn.fg,
  --     diag_INFO = DiagnosticInfo.fg,
  --     diag_HINT = DiagnosticHint.fg,
  --     winbar_fg = WinBar.fg,
  --     winbar_bg = WinBar.bg,
  --     winbarnc_fg = WinBarNC.fg,
  --     winbarnc_bg = WinBarNC.bg,
  --     tabline_bg = StatusLine.bg,
  --     tabline_fg = StatusLine.bg,
  --     buffer_fg = Comment.fg,
  --     buffer_path_fg = WinBarNC.fg,
  --     buffer_close_fg = Comment.fg,
  --     buffer_bg = StatusLine.bg,
  --     buffer_active_fg = Normal.fg,
  --     buffer_active_path_fg = WinBarNC.fg,
  --     buffer_active_close_fg = Error.fg,
  --     buffer_active_bg = Normal.bg,
  --     buffer_visible_fg = Normal.fg,
  --     buffer_visible_path_fg = WinBarNC.fg,
  --     buffer_visible_close_fg = Error.fg,
  --     buffer_visible_bg = Normal.bg,
  --     buffer_overflow_fg = Comment.fg,
  --     buffer_overflow_bg = StatusLine.bg,
  --     buffer_picker_fg = Error.fg,
  --     tab_close_fg = Error.fg,
  --     tab_close_bg = StatusLine.bg,
  --     tab_fg = TabLine.fg,
  --     tab_bg = TabLine.bg,
  --     tab_active_fg = TabLineSel.fg,
  --     tab_active_bg = TabLineSel.bg,
  --     inactive = HeirlineInactive.fg,
  --     normal = HeirlineNormal.fg,
  --     insert = HeirlineInsert.fg,
  --     visual = HeirlineVisual.fg,
  --     replace = HeirlineReplace.fg,
  --     command = HeirlineCommand.fg,
  --     terminal = HeirlineTerminal.fg,
  --   },
  --   attributes = {
  --     buffer_active = { bold = true, italic = true },
  --     buffer_picker = { bold = true },
  --     macro_recording = { bold = true },
  --     git_branch = { bold = true },
  --     git_diff = { bold = true },
  --   }
  --   icon_highlights = {
  --     breadcrumbs = false,
  --     file_icon = {
  --       tabline = function(self) return self.is_active or self.is_visible end,
  --       statusline = true,
  --       winbar = false,
  --     },
  --   }
  -- },
  lsp = {
    -- customize lsp formatting options
    formatting = {
      -- control auto formatting on save
      format_on_save = {
        enabled = false, -- enable or disable format on save globally
        allow_filetypes = { -- enable format on save for specified filetypes only
          -- "go",
        },
        ignore_filetypes = { -- disable format on save for specified filetypes
          -- "python",
        },
      },
      disabled = { -- disable formatting capabilities for the listed language servers
        -- "sumneko_lua",
      },
      timeout_ms = 1000, -- default format timeout
      -- filter = function(client) -- fully override the default formatting function
      --   return true
      -- end
    },
  },
 }
