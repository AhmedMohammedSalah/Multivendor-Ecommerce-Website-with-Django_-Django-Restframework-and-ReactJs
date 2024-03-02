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
    