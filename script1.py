from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.student-submissions.students.readonly']
client_id="236828613968-7nan4g7r1n93bkbl3obpo6pihoaekfc0.apps.googleusercontent.com"
client_secret="Fq6zH4EcxcCPd1-kDH3eQFcA"
def get_service_obj():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('classroom', 'v1', credentials=creds)
    return service

def operations():
    service=get_service_obj()
    # Call the Classroom API
    #results = service.courses().list(pageSize=10).execute()
    results = service.courses().courseWork().studentSubmissions().list(courseId='jh41e',courseWorkId='-',userId='prarthanaparu').execute()
    print(str(results))
    #courses = results.get('courses', [])
    #response = service.courses('https://classroom.googleapis.com/v1/courses/jh41e/students')
    '''
    print(response.text)
    if not courses:
        print('No courses found.')
    else:
        print('Courses:')
        for course in courses:
            print(course['name'])

    '''
if __name__ == '__main__':
    operations()
