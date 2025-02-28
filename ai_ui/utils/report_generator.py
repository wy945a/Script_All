from datetime import datetime

class ReportGenerator:
    def __init__(self):
        self.results = []

    def add_result(self, test_name, status, message=None):
        result = {
            'test_name': test_name,
            'status': status,
            'message': message,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.results.append(result)

    def generate_html_report(self, output_path):
        html_content = """
        <html>
        <head><title>Test Report</title></head>
        <body>
        <h1>Test Report</h1>
        <table border="1">
        <tr><th>Test Name</th><th>Status</th><th>Message</th><th>Timestamp</th></tr>
        """
        for result in self.results:
            html_content += f"""
            <tr>
                <td>{result['test_name']}</td>
                <td style="color:{'green' if result['status'] == 'Passed' else 'red'}">{result['status']}</td>
                <td>{result['message'] or ''}</td>
                <td>{result['timestamp']}</td>
            </tr>
            """
        html_content += """
        </table>
        </body>
        </html>
        """
        with open(output_path, 'w') as f:
            f.write(html_content)