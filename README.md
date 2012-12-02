## Introduction
This is a plugin for Gedit 3 that allows the line ending style of documents to be quickly ascertained and changed. It adds a small, dual-purpose combo box to the status bar which indicates the current document's line ending style and allows it to be changed:

![Screenshot](http://i.imgur.com/tI8zh.png)

## System-wide installation
*You will need root privileges. Alternatively, you can install the plugin for only yourself using the instructions below, in the "Local installation" section.*

 *  Download the v0.2 sources. You can either save & extract GitHub's automatically-generated tarball [`v0.2.tar.gz`](https://github.com/dtrebbien/gedit-line-ending-style-plugin/archive/v0.2.tar.gz) or clone the repository, verify my GPG signature of the `v0.2` tag, and check out `tags/v0.2`.
 *  In a terminal, `cd` into the directory containing the v0.2 sources.
 *  Configure the package. For most systems, the following configure line will work:

    <pre>
./configure --prefix=/usr
</pre>

    However, on 64-bit Fedora systems, you will need to override the libdir:
    
    <pre>
./configure --prefix=/usr --libdir=/usr/lib64
</pre>
 *  `make && sudo make install`

If users want the plugin enabled, they will need to enable it on the Gedit Preferences dialog.

## Local installation
Local installation of the plugin is for when you don't have root access or you only want to install it for yourself.

 0. You may need to create some directories if you haven't installed Gedit plugins locally before:

    <pre>
mkdir --parents ~/.local/share/gedit/plugins
</pre>
 1. Save [`lineendingstyle.plugin`](https://raw.github.com/dtrebbien/gedit-line-ending-style-plugin/0181c1eb07e407a54d31e577aead119ad12bfe1b/src/lineendingstyle.plugin) and [`lineendingstyle.py`](https://raw.github.com/dtrebbien/gedit-line-ending-style-plugin/0181c1eb07e407a54d31e577aead119ad12bfe1b/src/lineendingstyle.py) to `~/.local/share/gedit/plugins`
 2. Re-start Gedit.
 3. From the Edit menu, select "Preferences".
 4. On the Plugins tab, scroll down to the entry for "Line Ending Style" and check the checkbox.
 5. Click Close.

### Uninstallation
 0. From the Edit menu, select "Preferences".
 1. On the Plugins tab, scroll down to the entry for "Line Ending Style" and uncheck the checkbox.
 2. Close Gedit.
 3. Delete `lineendingstyle.plugin` and `lineendingstyle.py` from `~/.local/share/gedit/plugins`.

## Notes
 *  It is not currently possible to undo changing the line ending style using Ctrl+Z. If you want to change the line ending style back, just change it to the old style of line endings using the combo box in the status bar.
 *  If the current document is read-only, the line ending style combo box is disabled.
 *  The plugin was originally inspired by [Jeffery To](https://github.com/jefferyto)'s Newline Madness plugin for Gedit 2.

## License
<pre>
Copyright © 2012  Daniel Trebbien

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
</pre>

## Similar projects

 *  [Show and change line endings](http://plugins.netbeans.org/plugin/36810/show-and-change-line-endings) for NetBeans