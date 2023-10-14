"""
Author: Core447
Year: 2023

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This programm comes with ABSOLUTELY NO WARRANTY!

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
# Import Python modules
import os

# Import own modules
from src.backend.PageManagement.Page import Page

class PageManager:
    def __init__(self, settings_manager):
        self.settings_manager = settings_manager
        self.pages = dict()
    
    def load_pages(self) -> None:
        for page in os.listdir("pages"):
            page_path = os.path.join("pages", page)
            self.pages[page] = Page(page_path)
    
    def save_pages(self) -> None:
        for page in self.pages.values():
            page.save()

    def get_pages(self, remove_extension: bool = False) -> list:
        pages = list(self.pages.keys())
        if remove_extension:
            pages = [os.path.splitext(page)[0] for page in pages]
        return pages
    
    def get_default_page_for_deck(self, serial_number: str, remove_extension: bool = False) -> Page:
        page_settings = self.settings_manager.load_settings_from_file("settings/pages.json")
        for page in page_settings["default-pages"]:
            if page["deck"] == serial_number:
                if remove_extension:
                    return os.path.splitext(page["name"])[0]
                return self.pages[page["name"]]
        return None