from views import EntryView

class GetUrls:
    @staticmethod
    def fetch_urls(entry):
        entry.add_url_rule('/api/v1/entries/',
                              view_func=EntryView.as_view('getallentries'), defaults={'entry_id': None},
                              methods=['GET',])
        entry.add_url_rule('/api/v1/entries/<int:entry_id>/',
                              view_func=EntryView.as_view('getoneentry'),
                              methods=['GET',])
        entry.add_url_rule('/api/v1/entries/',view_func=EntryView.as_view('postentry'), methods=['POST',])
        entry.add_url_rule('/api/v1/entries/<int:event_id>/', view_func=EntryView.as_view('modifyanentry'), methods=['PUT',])