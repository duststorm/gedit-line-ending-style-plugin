# lineendingstyle.py generated automatically from lineendingstyle.py.in
# -*- Mode: Python; coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-
#
# Line Ending Style, a plugin for Gedit 3
# Copyright (C) 2012  Daniel Trebbien <dtrebbien@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import gettext
from gi.repository import GObject, Gdk, Gtk, Gedit

try:
	GeditStatusComboBox = Gedit.StatusComboBox
except:
	class GeditStatusComboBox(Gtk.EventBox):
		"""A pure PyGObject port of the GeditStatusComboBox class.

		Current with `gedit-status-combo-box.h` and `gedit-status-combo-box.c` from
		the tree for commit f167eb6 <http://git.gnome.org/browse/gedit/tree/?id=f167eb694e9c98f76a19aad7480f571e92bd6603>"""

		# Uncommenting the following line results in `sys:1: Warning: cannot register existing type `GeditStatusComboBox'`
		#__gtype_name__ = "GeditStatusComboBox"

		__gproperties__ = {
			"label": (str, "LABEL", "The label", None, GObject.PARAM_READWRITE)
		}

		__gsignals__ = {
			"changed": (GObject.SIGNAL_RUN_LAST, None, (Gtk.MenuItem,))
		}

		ITEM_TEXT_KEY = "GeditStatusComboBoxItemText"
		ACTIVATE_HANDLER_ID_KEY = "GeditStatusComboBoxActivateHandlerId"

		@classmethod
		def new(cls, label_text):
			return GeditStatusComboBox(label_text)

		def __init__(self, label_text):
			super(Gtk.EventBox, self).__init__()

			css = self.css = Gtk.CssProvider()
			css.load_from_data("* {\n" +
					"  -GtkButton-default-border : 0;\n" +
					"  -GtkButton-default-outside-border : 0;\n" +
					"  -GtkButton-inner-border: 0;\n" +
					"  -GtkWidget-focus-line-width : 0;\n" +
					"  -GtkWidget-focus-padding : 0;\n" +
					"  padding: 0;\n" +
					"}", -1)

			self.set_visible_window(True)

			frame = self.frame = Gtk.Frame()
			frame.show()

			button = self.button = Gtk.ToggleButton()
			button.set_relief(Gtk.ReliefStyle.NONE)
			button.show()

			self.__set_shadow_type()

			hbox = self.hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 3)
			hbox.show()

			self.add(frame)
			frame.add(button)
			button.add(hbox)

			label = self.label = Gtk.Label.new("")
			label.show()
			label.set_single_line_mode(True)
			label.set_halign(Gtk.Align.START)

			hbox.pack_start(label, False, True, 0)

			item = self.item = Gtk.Label.new("")
			item.show()
			item.set_single_line_mode(True)
			item.set_halign(Gtk.Align.START)

			hbox.pack_start(item, True, True, 0)

			arrow = self.arrow = Gtk.Arrow.new(Gtk.ArrowType.DOWN, Gtk.ShadowType.NONE)
			arrow.show()

			hbox.pack_start(arrow, False, True, 0)

			menu = self.menu = Gtk.Menu()
			menu.attach_to_widget(self, self.__menu_detached)

			button.connect("button-press-event", self.__button_press_event)
			button.connect("key-press-event", self.__key_press_event)
			menu.connect("deactivate", self.__menu_deactivate)

			# Make it as small as possible.
			context = button.get_style_context()
			context.add_provider(css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

			context = frame.get_style_context()
			context.add_provider(css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

		def __del__(self):
			self.menu.detach()

		def __set_shadow_type(self):
			# This is a hack needed to use the shadow type of a statusbar.
			statusbar = Gtk.Statusbar()
			context = statusbar.get_style_context()

			shadow_type_val = GObject.Value()
			shadow_type_val.init(Gtk.ShadowType)
			context.get_style_property("shadow-type", shadow_type_val)
			self.frame.set_shadow_type(shadow_type_val.get_enum())

			del statusbar

		def __menu_detached(self, menu):
			self.menu = None

		def __show_menu(self, button, time):
			menu = self.menu
			request, _ = menu.get_preferred_size()

			# Do something relative to our own height here. Maybe we can do better.
			allocation = self.get_allocation()
			max_height = allocation.height * 20

			if request.height > max_height:
				menu.set_size_request(-1, max_height)
				menu.get_toplevel().set_size_request(-1, max_height)

			def menu_position_func(menu, push_in, data):
				request, _ = menu.get_toplevel().get_preferred_size()

				_, x, y = self.get_window().get_origin()

				# Make the menu at least as wide as the widget.
				allocation = self.get_allocation()
				if request.width < allocation.width:
					menu.set_size_request(allocation.width, -1)

				# Position it above the widget.
				y -= request.height

				return (x, y, False)

			menu.popup(None, None, menu_position_func, None, button, time)

			self.button.set_active(True)

			if hasattr(self, "current_item"):
				menu.select_item(self.current_item)

		def __button_press_event(self, widget, event):
			if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 1:
				self.__show_menu(event.button, event.time)
				return True

			return False

		def __key_press_event(self, widget, event):
			if event.keyval == Gdk.KEY_Return or event.keyval == Gdk.KEY_ISO_Enter or \
					event.keyval == Gdk.KEY_KP_Enter or event.keyval == Gdk.KEY_space or \
					event.keyval == Gdk.KEY_KP_Space:
				self.__show_menu(1, event.time)
				return True

			return False

		def __menu_deactivate(self, menu):
			self.button.set_active(False)

		def do_changed(self, item):
			text = item.get_data(GeditStatusComboBox.ITEM_TEXT_KEY)
			if text != None:
				self.item.set_markup(text)
				self.current_item = item

		def get_label(self):
			return self.label.get_label()

		def set_label(self, label_text):
			if label_text:
				label_text = "  " + label_text + ": "
			else:
				label_text = "  "
			self.label.set_markup(label_text)

		def add_item(self, item, text):
			self.menu.append(item)

			self.set_item_text(item, text)

			activate_handler_id = item.connect("activate", lambda item: self.set_item(item))
			item.set_data(GeditStatusComboBox.ACTIVATE_HANDLER_ID_KEY, activate_handler_id)

		def remove_item(self, item):
			activate_handler_id = item.get_data(GeditStatusComboBox.ACTIVATE_HANDLER_ID_KEY)
			if activate_handler_id != None:
				item.disconnect(activate_handler_id)
			item.set_data(GeditStatusComboBox.ACTIVATE_HANDLER_ID_KEY, None)
			item.set_data(GeditStatusComboBox.ITEM_TEXT_KEY, None)
			self.menu.remove(item)

		def get_items(self):
			return self.menu.get_children()

		def get_item_text(self, item):
			return item.get_data(GeditStatusComboBox.ITEM_TEXT_KEY)

		def set_item_text(self, item, text):
			item.set_data(GeditStatusComboBox.ITEM_TEXT_KEY, text)

		def set_item(self, item):
			self.emit("changed", item)

		def get_item_label(self):
			return self.item

		def do_get_property(self, property):
			if property.name == "label":
				return self.get_label()
			else:
				raise AttributeError, "unknown property %s" % property.name

		def do_set_property(self, property, value):
			if property.name == "label":
				self.set_label(value)
			else:
				raise AttributeError, "unknown property %s" % property.name

class LineEndingStylePluginUi:
	ITEM_VALUE_KEY = "GeditLineEndingStylePluginUiItemValue"
	NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY = "GeditLineEndingStylePluginUiNotifyNewline-TypeHandlerId"

	def __init__(self, window):
		self.window = window

	def merge(self):
		action_group = self.action_group = Gtk.ActionGroup("GeditLineEndingStylePluginActions")
		action_group.set_translation_domain("gedit-line-ending-style-plugin")
		_ = lambda string: action_group.translate_string(string)

		window = self.window
		statusbar = window.get_statusbar()
		sb_combo = self.sb_combo = GeditStatusComboBox.new(None)

		entries = [
					("LineEndingStylePluginStatusComboToLFItem", "Unix/Linux", "Switch to Unix/Linux-style line endings (LF)",
							Gedit.DocumentNewlineType.LF, "LF"),
					("LineEndingStylePluginStatusComboToCRItem", "Mac OS Classic", "Switch to Mac OS Classic-style line endings (CR)",
							Gedit.DocumentNewlineType.CR, "CR"),
					("LineEndingStylePluginStatusComboToCRLFItem", "Windows", "Switch to Windows-style line endings (CRLF)",
							Gedit.DocumentNewlineType.CR_LF, "CRLF")
				]
		activate_callback = lambda item: self.set_active_document_newline_type(item.get_data(LineEndingStylePluginUi.ITEM_VALUE_KEY))
		for entry in entries:
			action = Gtk.Action(entry[0],
					_(entry[1]),
					_(entry[2]),
					None)
			action_group.add_action(action)
			item = action.create_menu_item()
			item.set_data(LineEndingStylePluginUi.ITEM_VALUE_KEY, entry[3])
			item.connect("activate", activate_callback)
			sb_combo.add_item(item, _(entry[4]))

		sb_combo.show_all()
		statusbar.pack_end(sb_combo, False, True, 0)

		doc = window.get_active_document()
		if doc:
			self.update_state_per_document(doc)

		self.tab_added_handler_id = window.connect("tab-added",
				lambda window, tab: self.connect_notify_newline_type_handler(tab.get_document()))
		self.active_tab_changed_handler_id = window.connect("active-tab-changed",
				lambda window, tab: self.update_state_per_document(tab.get_document()))
		self.tab_removed_handler_id = window.connect("tab-removed",
				lambda window, tab: self.disconnect_notify_newline_type_handler(tab.get_document()))

		for doc in window.get_documents():
			self.connect_notify_newline_type_handler(doc)

	def connect_notify_newline_type_handler(self, doc):
		notify_newline_type_handler_id = doc.connect("notify::newline-type", lambda doc, pspec: self.update_state_per_document(doc))
		doc.set_data(LineEndingStylePluginUi.NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY, notify_newline_type_handler_id)

	def disconnect_notify_newline_type_handler(self, doc):
		notify_newline_type_handler_id = doc.get_data(LineEndingStylePluginUi.NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY)
		doc.set_data(LineEndingStylePluginUi.NOTIFY_NEWLINE_TYPE_HANDLER_ID_KEY, None)
		if notify_newline_type_handler_id != None:
			doc.disconnect(notify_newline_type_handler_id)

	def update_state_per_document(self, doc):
		sb_combo = self.sb_combo

		if doc:
			nl_type = doc.get_property("newline-type")

			for item in sb_combo.get_items():
				if item.get_data(LineEndingStylePluginUi.ITEM_VALUE_KEY) == nl_type:
					sb_combo.set_item(item)
					break

			sb_combo.show()
		else:
			sb_combo.hide()

	def set_active_document_newline_type(self, nl_type):
		doc = self.window.get_active_document()
		if doc:
			doc.set_property("newline-type", nl_type)

	def update_ui(self):
		doc = self.window.get_active_document()
		if doc:
			b = not doc.get_readonly()
			self.sb_combo.set_sensitive(b)
		self.update_state_per_document(doc)

	def unmerge(self):
		window = self.window
		for doc in window.get_documents():
			self.disconnect_notify_newline_type_handler(doc)
		window.disconnect(self.tab_removed_handler_id); del self.tab_removed_handler_id
		window.disconnect(self.active_tab_changed_handler_id); del self.active_tab_changed_handler_id
		window.disconnect(self.tab_added_handler_id); del self.tab_added_handler_id
		Gtk.HBox.remove(window.get_statusbar(), self.sb_combo); del self.sb_combo
		del self.window

class LineEndingStylePlugin(GObject.Object, Gedit.WindowActivatable):
	__gtype_name__ = "LineEndingStylePlugin"

	UI_KEY = "GeditLineEndingStylePluginUi"

	window = GObject.property(type = Gedit.Window)

	def __init__(self):
		pass

	def do_activate(self):
		window = self.window
		ui = LineEndingStylePluginUi(window)
		ui.merge()
		window.set_data(LineEndingStylePlugin.UI_KEY, ui)
		pass

	def do_deactivate(self):
		window = self.window
		ui = window.get_data(LineEndingStylePlugin.UI_KEY)
		window.set_data(LineEndingStylePlugin.UI_KEY, None)
		ui.unmerge()
		pass

	def do_update_state(self):
		window = self.window
		ui = window.get_data(LineEndingStylePlugin.UI_KEY)
		ui.update_ui()
		pass

gettext.bindtextdomain("gedit-line-ending-style-plugin", "/usr/share/locale")