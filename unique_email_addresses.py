class Solution:
    '''https://leetcode.com/problems/unique-email-addresses/submissions/'''
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set(self.filter_email_address(email) for email in emails)
        return len(unique_emails)

    def filter_email_address(self, address):
        name, domain = address.split('@')
        filtered_name = ''
        for char in name:
            if char == '+':
                break
            elif char != '.':
                filtered_name += char
        return filtered_name + '@' + domain