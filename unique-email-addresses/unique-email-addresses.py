class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            unique_emails.add(self.normalize_email(email))
            
        return len(unique_emails)
            
    def normalize_email(self, email: str):
        email_name, email_domain = email.split("@")
        
        email_name = email_name.split('+')[0]
        email_name = email_name.replace('.','')
        
        return email_name + '@' + email_domain