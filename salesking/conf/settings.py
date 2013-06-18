#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# global predefined settings
SK_ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
SCHEMA_ROOT = os.path.join(SK_ROOT, "schemes")

AUTH_URL = u"/oauth/authorize"
ACCESS_TOKEN_URL = u"/oauth/token"



# get user-settings (backwards-comptible)
try:
    from salesking.conf.local_settings import SALESKING_API
except ImportError as e:
    raise Exception("please create a salesking.conf.local_settings")


API = {
    # YOUR APPID
    u"app_id": SALESKING_API['APP_ID'],
    # YOUR APP SECRET
    u"app_secret": SALESKING_API['APP_SECRET'],
    u"app_scope": u"api/clients:write",
    # YOUR SALESKING SUBDOMAIN
    u"sk_subdomain": SALESKING_API['SK_SUBDOMAIN'],

    u"base_url": SALESKING_API['BASE_URL'],
    u"oauth_redirect_url": u"http://localhost/",
    u"debug": True,
    u"use_oauth": True,
    u"sk_user": SALESKING_API['SK_USER'],
    u"sk_pw": SALESKING_API['SK_PASSWORD'],
}
