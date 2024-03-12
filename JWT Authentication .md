working with JWT Authentication 
    [install-it]
        >>  pip install djangorestframework-simplejwt 
        >>  python -m pip install --upgrade pip wheel 
        >>  python -m pip install httpie   
    [configrations]
        [settings.py]
            [1]add 'rest_framework_simplejwt' to installed_apps 
            [2]add this to REST_FRAMEWORK
                    'DEFAULT_AUTHENTICATION_CLASSES': (
                         'rest_framework_simplejwt.authentication.JWTAuthentication',
                    )
        [urls.py]
            [1]from rest_framework_simplejwt import views as jwt_views
            [2] path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
                path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    [working-on-it]
        [generate-token]  
            [run]>> http post http://127.0.0.1:8000/api/token/ username=admin password=1234
            [response]>> HTTP/1.1 200 OK
                        {
                            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5Mzc3OTY5LCJpYXQiOjE3MDkzNzc2NjksImp0aSI6IjNlNmFhNDAyN2VhMTRjYzlhMWIwYWMwZDRmMzdmOWU3IiwidXNlcl9pZCI6MX0.KjsaHlAi19XCB8hMwiACJ4_jaVEiWav8dFA8h5o4H7o",
                            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTQ2NDA2OSwiaWF0IjoxNzA5Mzc3NjY5LCJqdGkiOiJmN2UwMGVhZDllNDY0NmVhYTVmMjZlZTRmMzc2NDJkNSIsInVzZXJfaWQiOjF9.21wjwpdYKJsK3Tu7x5EM4JxubH4dw-bf5-0IK7NUlEY"
                        }
        [test-it]
            [run]>> http http://127.0.0.1:8000/api/vendors/  "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5Mzc3OTY5LCJpYXQiOjE3MDkzNzc2NjksImp0aSI6IjNlNmFhNDAyN2VhMTRjYzlhMWIwYWMwZDRmMzdmOWU3IiwidXNlcl9pZCI6MX0.KjsaHlAi19XCB8hMwiACJ4_jaVEiWav8dFA8h5o4H7o"
            [result]>> HTTP/1.1 200 OK
                    [
                        {
                            "address": "S9KG2WAj_@BTC7$S9KG2WAj_@BTC7$S9KG2WAj_@BTC7$S9KG2WAj_@BTC7$",
                            "id": 1,
                            "user": {
                                "date_joined": "2024-03-01T11:36:23Z",
                                "email": "",
                                "first_name": "",
                                "groups": [],
                                "id": 2,
                                "is_active": true,
                                "is_staff": false,
                                "is_superuser": false,
                                "last_login": null,
                                "last_name": "",
                                "password": "pbkdf2_sha256$720000$Ksimjx5wUHqMdrtcCeM4pA$/WGWn7Xa8qCyo1oG23V/tvnJjJTiYtC/+7azbnNl/BU=",
                                "user_permissions": [],
                                "username": "testVendor"
                            }
                        }
                    ]
            [run]
                >>http http://127.0.0.1:8000/api/token/refresh/  refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTQ2NjkwMywiaWF0IjoxNzA5MzgwNTAzLCJqdGkiOiJjMzg4MzM0ZTI5YWU0ZmViYWNhNTE1N2I1MDA2MWZmYSIsInVzZXJfaWQiOjF9.kbdIqDEHE9X5S781kn26OGdomoQGV62rV5ngMpkVrVU
            [result]>>HTTP/1.1 200 OK
                {
                    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5MzgwOTg3LCJpYXQiOjE3MDkzODA1MDMsImp0aSI6ImZiYmMwNzNkMjE3NTRhMzhhNWUzNGU4MjBkNTVmMTE5IiwidXNlcl9pZCI6MX0.bTTRebBFArrD7Mu365Nw3ftLcXnMjlYqCFHFoKJmEeY"
                }