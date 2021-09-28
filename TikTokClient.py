#!/usr/bin/python
# -*- coding: utf-8 -*-
# TikTok Premium API client.
#
# TERMS OF USE:
# - This code is in no way affiliated with, authorized, maintained, sponsored
#   or endorsed by TikTok or any of its affiliates or subsidiaries.  This is
#   an independent and unofficial API.  Use at your own risk.
# - We do NOT support or tolerate anyone who wants to use this API to send spam
#   or commit other online crimes.
# - You will NOT use this API for marketing or other abusive purposes (spam,
#   botting, harassment, massive bulk messaging...).  For education purposes
#   only.
#
# @author revpy200, revpy200@gmail.com

import requests as r

class TikTokApiClient:

    protocol = "http"
    host = "localhost"
    port = 4444

    base_url = protocol + "://" + host + ":" + str(port)

    tok_proxy = ""
    api_token = ""

    def __init__(self, proxy, token) -> None:
        self.tok_proxy = proxy
        self.api_token = token

    def device_register(self):
        path = "/device-register"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

    def account_register(self, install_id, device_id, openudid, operator_id, email, password):
        path = "/account-register"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token,
            'install-id': install_id,
            'device-id': device_id,
            'openudid': openudid,
            'operator-id': operator_id,
            'email': email,
            'password': password
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

    def account_register_verify_code(self, install_id, device_id, openudid, operator_id, email, password, code):
        path = "/register-verify-code"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token,
            'install-id': install_id,
            'device-id': device_id,
            'openudid': openudid,
            'operator-id': operator_id,
            'email': email,
            'password': password,
            'code' : str(code)
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

    def account_register_verify_age(self, install_id, device_id, openudid, operator_id, birthday):
        path = "/register-verify-age"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token,
            'install-id': install_id,
            'device-id': device_id,
            'openudid': openudid,
            'operator-id': operator_id,
            'birthday': birthday
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

    def account_register_verify_email_registered(self, install_id, device_id, openudid, operator_id, email):
        path = "/register-verify-email-registered"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token,
            'install-id': install_id,
            'device-id': device_id,
            'openudid': openudid,
            'operator-id': operator_id,
            'email': email
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

    def account_login_username(self, install_id, device_id, openudid, operator_id, username, password):
        path = "/login-username"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token,
            'install-id': install_id,
            'device-id': device_id,
            'openudid': openudid,
            'operator-id': operator_id,
            'username': username,
            'password' : password
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

    def account_login_email(self, install_id, device_id, openudid, operator_id, email, password):
        path = "/login-email"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token,
            'install-id': install_id,
            'device-id': device_id,
            'openudid': openudid,
            'operator-id': operator_id,
            'email': email,
            'password' : password
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

    def post_like(self, install_id, device_id, openudid, operator_id, aweme_id, cookie, uid):
        path = "/like-post"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token,
            'install-id': install_id,
            'device-id': device_id,
            'openudid': openudid,
            'operator-id': operator_id,
            'aweme_id': str(aweme_id),
            'cookie': cookie,
            'uid': str(uid)
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

    def post_comment(self, install_id, device_id, openudid, operator_id, aweme_id, text, cookie, uid):
        path = "/post-comment"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token,
            'install-id': install_id,
            'device-id': device_id,
            'openudid': openudid,
            'operator-id': operator_id,
            'aweme_id': str(aweme_id),
            'text' : text,
            'cookie': cookie,
            'uid': str(uid)
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

    def user_follow(self, install_id, device_id, openudid, operator_id, sec_userid, user_id, cookie, uid):
        path = "/follow-user"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token,
            'install-id': install_id,
            'device-id': device_id,
            'openudid': openudid,
            'operator-id': operator_id,
            'sec_userid': str(sec_userid),
            'user_id': str(user_id),
            'cookie': cookie,
            'uid': str(uid)
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

    def user_unfollow(self, install_id, device_id, openudid, operator_id, sec_userid, user_id, cookie, uid):
        path = "/unfollow-user"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token,
            'install-id': install_id,
            'device-id': device_id,
            'openudid': openudid,
            'operator-id': operator_id,
            'sec_userid': str(sec_userid),
            'user_id': str(user_id),
            'cookie': cookie,
            'uid': str(uid)
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)
