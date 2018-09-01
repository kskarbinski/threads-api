define({ "api": [
  {
    "type": "DELETE",
    "url": "/threads/applications/<String:application_id>",
    "title": "Cancel sent thread application",
    "description": "<p>Cancel sent thread application by id</p>",
    "group": "Thread",
    "version": "0.0.0",
    "filename": "app_routes/threads/applications/application_id/threads_applications_application_id_route.py",
    "groupTitle": "Thread",
    "name": "DeleteThreadsApplicationsStringApplication_id"
  },
  {
    "type": "DELETE",
    "url": "/threads/<String:thread_id>",
    "title": "Delete thread",
    "group": "Thread",
    "description": "<p>Delete thread by id as thread owner</p>",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/threads_thread_id_route.py",
    "groupTitle": "Thread",
    "name": "DeleteThreadsStringThread_id"
  },
  {
    "type": "DELETE",
    "url": "/threads/<String:thread_id>/invitations/<String:invitation_id>",
    "title": "Cancel sent thread invitation",
    "group": "Thread",
    "description": "<p>Cancel sent thread invitation</p>",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/invitations/invitation_id/threads_thread_id_invitations_invitation_id_route.py",
    "groupTitle": "Thread",
    "name": "DeleteThreadsStringThread_idInvitationsStringInvitation_id"
  },
  {
    "type": "DELETE",
    "url": "/threads/<String:thread_id>/messages/<String:message_id>",
    "title": "Remove thread message",
    "group": "Thread",
    "description": "<p>Remove thread message as message owner</p>",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/messages/message_id/threads_thread_id_messages_message_id_route.py",
    "groupTitle": "Thread",
    "name": "DeleteThreadsStringThread_idMessagesStringMessage_id"
  },
  {
    "type": "GET",
    "url": "/threads",
    "title": "Get threads",
    "description": "<p>Get last 100 threads created</p>",
    "group": "Thread",
    "version": "0.0.0",
    "filename": "app_routes/threads/threads_route.py",
    "groupTitle": "Thread",
    "name": "GetThreads"
  },
  {
    "type": "GET",
    "url": "/threads/applications",
    "title": "Get sent thread applications",
    "description": "<p>Get last 100 sent thread applications for current user</p>",
    "group": "Thread",
    "version": "0.0.0",
    "filename": "app_routes/threads/applications/threads_applications_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsApplications"
  },
  {
    "type": "GET",
    "url": "/threads/applications/<String:application_id>",
    "title": "Get sent thread application",
    "description": "<p>Get sent thread application by id</p>",
    "group": "Thread",
    "version": "0.0.0",
    "filename": "app_routes/threads/applications/application_id/threads_applications_application_id_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsApplicationsStringApplication_id"
  },
  {
    "type": "GET",
    "url": "/threads/invitations",
    "title": "Get received thread invitations",
    "description": "<p>Get last 100 received thread applications for current user</p>",
    "group": "Thread",
    "version": "0.0.0",
    "filename": "app_routes/threads/invitations/threads_invitations_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsInvitations"
  },
  {
    "type": "GET",
    "url": "/threads/invitations/<String:invitation_id>",
    "title": "Get received thread invitation",
    "description": "<p>Get received thread invitation by id</p>",
    "group": "Thread",
    "version": "0.0.0",
    "filename": "app_routes/threads/invitations/invitation_id/threads_invitations_invitation_id_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsInvitationsStringInvitation_id"
  },
  {
    "type": "GET",
    "url": "/threads/<String:thread_id>",
    "title": "Get thread",
    "group": "Thread",
    "description": "<p>Get thread by id</p>",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/threads_thread_id_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsStringThread_id"
  },
  {
    "type": "GET",
    "url": "/threads/<String:thread_id>/applications",
    "title": "Get received thread applications",
    "group": "Thread",
    "description": "<p>Get received thread applications as thread owner</p>",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/applications/threads_thread_id_applications_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsStringThread_idApplications"
  },
  {
    "type": "GET",
    "url": "/threads/<String:thread_id>/applications/<String:application_id>",
    "title": "Get received thread application",
    "group": "Thread",
    "description": "<p>Get received thread application by id</p>",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/applications/application_id/threads_thread_id_applications_application_id_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsStringThread_idApplicationsStringApplication_id"
  },
  {
    "type": "GET",
    "url": "/threads/<String:thread_id>/invitations",
    "title": "Get sent thread invitations",
    "group": "Thread",
    "description": "<p>Get sent thread invitations</p>",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/invitations/threads_thread_id_invitations_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsStringThread_idInvitations"
  },
  {
    "type": "GET",
    "url": "/threads/<String:thread_id>/invitations/<String:invitation_id>",
    "title": "Get sent thread invitation",
    "group": "Thread",
    "description": "<p>Get sent thread invitation</p>",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/invitations/invitation_id/threads_thread_id_invitations_invitation_id_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsStringThread_idInvitationsStringInvitation_id"
  },
  {
    "type": "GET",
    "url": "/threads/<String:thread_id>/messages",
    "title": "Get thread messages",
    "group": "Thread",
    "description": "<p>Get last 100 thread messages as member of thread</p>",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/messages/threads_thread_id_messages_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsStringThread_idMessages"
  },
  {
    "type": "GET",
    "url": "/threads/<String:thread_id>/messages/<String:message_id>",
    "title": "Get thread message",
    "group": "Thread",
    "description": "<p>Get thread message as member of thread</p>",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/messages/message_id/threads_thread_id_messages_message_id_route.py",
    "groupTitle": "Thread",
    "name": "GetThreadsStringThread_idMessagesStringMessage_id"
  },
  {
    "type": "POST",
    "url": "/threads",
    "title": "Create thread",
    "group": "Thread",
    "parameter": {
      "fields": {
        "JSON param": [
          {
            "group": "JSON param",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Name of the thread. Has to be unique, must not be a number, length 2-50</p>"
          },
          {
            "group": "JSON param",
            "type": "Boolean",
            "optional": false,
            "field": "private",
            "description": "<p>Whether the thread is to be private or not</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "app_routes/threads/threads_route.py",
    "groupTitle": "Thread",
    "name": "PostThreads"
  },
  {
    "type": "POST",
    "url": "/threads/invitations/<String:invitation_id>",
    "title": "Accept or reject thread invitation",
    "group": "Thread",
    "parameter": {
      "fields": {
        "JSON param": [
          {
            "group": "JSON param",
            "type": "Boolean",
            "optional": false,
            "field": "accept",
            "description": "<p>Accept or reject the invitation</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "app_routes/threads/invitations/invitation_id/threads_invitations_invitation_id_route.py",
    "groupTitle": "Thread",
    "name": "PostThreadsInvitationsStringInvitation_id"
  },
  {
    "type": "POST",
    "url": "/threads/<String:thread_id>/applications/<String:application_id>",
    "title": "Accept or reject received thread application",
    "group": "Thread",
    "parameter": {
      "fields": {
        "JSON param": [
          {
            "group": "JSON param",
            "type": "Boolean",
            "optional": false,
            "field": "accept",
            "description": "<p>Accept or reject the application</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/applications/application_id/threads_thread_id_applications_application_id_route.py",
    "groupTitle": "Thread",
    "name": "PostThreadsStringThread_idApplicationsStringApplication_id"
  },
  {
    "type": "POST",
    "url": "/threads/<String:thread_id>/apply",
    "title": "Apply to thread",
    "group": "Thread",
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/apply/threads_thread_id_apply_route.py",
    "groupTitle": "Thread",
    "name": "PostThreadsStringThread_idApply"
  },
  {
    "type": "POST",
    "url": "/threads/<String:thread_id>/invite",
    "title": "Invite users to thread",
    "group": "Thread",
    "parameter": {
      "fields": {
        "JSON param": [
          {
            "group": "JSON param",
            "type": "String[]",
            "optional": false,
            "field": "users",
            "description": "<p>List of user ids</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/invite/threads_thread_id_invite_route.py",
    "groupTitle": "Thread",
    "name": "PostThreadsStringThread_idInvite"
  },
  {
    "type": "POST",
    "url": "/threads/<String:thread_id>/kick",
    "title": "Kick users from thread",
    "group": "Thread",
    "parameter": {
      "fields": {
        "JSON param": [
          {
            "group": "JSON param",
            "type": "String[]",
            "optional": false,
            "field": "users",
            "description": "<p>List of user ids</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/kick/threads_thread_id_kick_route.py",
    "groupTitle": "Thread",
    "name": "PostThreadsStringThread_idKick"
  },
  {
    "type": "POST",
    "url": "/threads/<String:thread_id>/messages",
    "title": "Send message in thread",
    "group": "Thread",
    "description": "<p>Send message in thread as thread owner</p>",
    "parameter": {
      "fields": {
        "JSON param": [
          {
            "group": "JSON param",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>Message to send. Length 1-300</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/messages/threads_thread_id_messages_route.py",
    "groupTitle": "Thread",
    "name": "PostThreadsStringThread_idMessages"
  },
  {
    "type": "POST",
    "url": "/threads/<String:thread_id>/messages/<String:message_id>",
    "title": "Edit thread message",
    "group": "Thread",
    "description": "<p>Edit thread message as message owner</p>",
    "parameter": {
      "fields": {
        "JSON param": [
          {
            "group": "JSON param",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>New message. Length 1-300</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "app_routes/threads/thread_id/messages/message_id/threads_thread_id_messages_message_id_route.py",
    "groupTitle": "Thread",
    "name": "PostThreadsStringThread_idMessagesStringMessage_id"
  },
  {
    "type": "GET",
    "url": "/user",
    "title": "Get user",
    "group": "User",
    "description": "<p>Get current user details</p>",
    "version": "0.0.0",
    "filename": "app_routes/user/user_route.py",
    "groupTitle": "User",
    "name": "GetUser"
  },
  {
    "type": "GET",
    "url": "/users",
    "title": "Get users",
    "group": "User",
    "description": "<p>Get last 100 created users</p>",
    "version": "0.0.0",
    "filename": "app_routes/users/users_route.py",
    "groupTitle": "User",
    "name": "GetUsers"
  },
  {
    "type": "GET",
    "url": "/users/<String:user_id>",
    "title": "Get user by id",
    "group": "User",
    "description": "<p>Get user details by id</p>",
    "version": "0.0.0",
    "filename": "app_routes/users/user_id/users_user_id_route.py",
    "groupTitle": "User",
    "name": "GetUsersStringUser_id"
  },
  {
    "type": "GET",
    "url": "/users/<String:username>",
    "title": "Get user by username",
    "group": "User",
    "description": "<p>Get user details by username</p>",
    "version": "0.0.0",
    "filename": "app_routes/users/user_name/users_user_name_route.py",
    "groupTitle": "User",
    "name": "GetUsersStringUsername"
  },
  {
    "type": "GET",
    "url": "/validate/<String:username>",
    "title": "Validate username",
    "group": "User",
    "description": "<p>Validate username. Check whether it's already taken and has correct format</p>",
    "version": "0.0.0",
    "filename": "app_routes/validate/username/validate_username_route.py",
    "groupTitle": "User",
    "name": "GetValidateStringUsername"
  },
  {
    "type": "POST",
    "url": "/signup",
    "title": "Signup",
    "group": "User",
    "parameter": {
      "fields": {
        "JSON param": [
          {
            "group": "JSON param",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Username. Has to be unique, cannot be a number, length 2-20</p>"
          },
          {
            "group": "JSON param",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Password. Length 4-20</p>"
          },
          {
            "group": "JSON param",
            "type": "String",
            "optional": false,
            "field": "firstname",
            "description": "<p>First name. Length 2-20</p>"
          },
          {
            "group": "JSON param",
            "type": "String",
            "optional": false,
            "field": "lastname",
            "description": "<p>Last name. Length 2-50</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "app_routes/signup/signup_route.py",
    "groupTitle": "User",
    "name": "PostSignup"
  }
] });
