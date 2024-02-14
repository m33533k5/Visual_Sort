import configparser
import os

import tooltip
from constants import WHITE, LIGHT_GRAY, BUTTON, LABEL, GENERAL, TOOLTIP


class Translations:

    def load_translations(self, language):
        """
        Lädt die Übersetzungstexte aus einer Properties-Datei basierend auf der gewählten Sprache.

        :param language: Der Sprachcode der zu ladenden Übersetzungen (z.B. 'en', 'de').
        :return: Ein configparser Objekt mit den geladenen Übersetzungen.
        """
        # Bestimme das Verzeichnis des aktuellen Skripts, um den Pfad zur Übersetzungsdatei zu finden.
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Konstruiere den Pfad zur entsprechenden Properties-Datei.
        properties_file_path = os.path.join(current_directory, 'properties', f'{language}.properties')

        # Initialisiere configparser und lade die Übersetzungen aus der Datei.
        translations = configparser.ConfigParser()
        translations.read(properties_file_path)
        return translations

    def update_ui_with_translations(self, translations, ui_components):
        """
        Aktualisiert die UI-Komponenten mit den entsprechenden Übersetzungen.

        :param translations: Das configparser Objekt mit den geladenen Übersetzungen.
        :param ui_components: Ein Objekt, das die UI-Komponenten enthält, die aktualisiert werden sollen.
        """

        # Aktualisiere den Titel des Fensters mit der übersetzten Zeichenkette.
        ui_components.window.title(translations.get(GENERAL, 'window_title'))

        # Aktualisiere Texte und Tooltips für jede UI-Komponente.
        # Für jede Komponente wird der Text aus den Übersetzungen geladen und als Tooltip hinzugefügt.
        ui_components.label_algorithm.config(text=translations.get(LABEL, 'label_algorithm'), bg=WHITE)
        tooltip.ToolTip.create_tooltip(ui_components.label_algorithm, translations.get(TOOLTIP, 'tooltip_label_algorithm'))
        tooltip.ToolTip.create_tooltip(ui_components.algo_menu, translations.get(TOOLTIP, 'tooltip_field_algorithm'))

        ui_components.label_speed.config(text=translations.get(LABEL, 'label_speed'), bg=WHITE)
        tooltip.ToolTip.create_tooltip(ui_components.label_speed, translations.get(TOOLTIP, 'tooltip_label_speed'))
        tooltip.ToolTip.create_tooltip(ui_components.speed_menu, translations.get(TOOLTIP, 'tooltip_field_speed'))

        ui_components.label_size.config(text=translations.get(LABEL, 'label_size'), bg=WHITE)
        tooltip.ToolTip.create_tooltip(ui_components.label_size, translations.get(TOOLTIP, 'tooltip_label_size'))
        tooltip.ToolTip.create_tooltip(ui_components.size_entry, translations.get(TOOLTIP, 'tooltip_field_size'))

        ui_components.label_steps.config(text=translations.get(LABEL, 'label_steps'), bg=WHITE)
        tooltip.ToolTip.create_tooltip(ui_components.label_steps, translations.get(TOOLTIP, 'tooltip_label_steps'))
        tooltip.ToolTip.create_tooltip(ui_components.size_steps, translations.get(TOOLTIP, 'tooltip_field_steps'))

        ui_components.label_ranking.config(text=translations.get(LABEL, 'label_ranking'), bg=WHITE)
        tooltip.ToolTip.create_tooltip(ui_components.label_ranking, translations.get(TOOLTIP, 'tooltip_label_ranking'))
        tooltip.ToolTip.create_tooltip(ui_components.text_ranking, translations.get(TOOLTIP, 'tooltip_field_ranking'))

        ui_components.button_generate.config(text=translations.get(BUTTON, 'button_generate'), bg=LIGHT_GRAY)
        tooltip.ToolTip.create_tooltip(ui_components.button_generate, translations.get(TOOLTIP, 'tooltip_button_generate'))

        ui_components.button_sort.config(text=translations.get(BUTTON, 'button_sort'), bg=LIGHT_GRAY)
        tooltip.ToolTip.create_tooltip(ui_components.button_sort, translations.get(TOOLTIP, 'tooltip_button_sort'))

        ui_components.button_german_translation.config(text=translations.get(BUTTON, 'button_german_translation'), bg=LIGHT_GRAY)
        ui_components.button_english_translation.config(text=translations.get(BUTTON, 'button_english_translation'), bg=LIGHT_GRAY)

    def set_language(self, language_code, ui_components):
        """
        Setzt die Anwendungssprache und aktualisiert die UI entsprechend.

        :param language_code: Der Sprachcode, der gesetzt werden soll (z.B. 'en', 'de').
        :param ui_components: Ein Objekt, das die UI-Komponenten enthält, die aktualisiert werden sollen.
        """
        # Lade die Übersetzungen für die angegebene Sprache.
        translations = self.load_translations(language_code)
        # Aktualisiere die UI-Komponenten mit den geladenen Übersetzungen.
        self.update_ui_with_translations(translations, ui_components)
