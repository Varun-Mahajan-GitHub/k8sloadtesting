from locust import FastHttpUser, task, between


class AudioDrmApi(FastHttpUser):

    @task()
    def check_auth_api(self):
        url = "/getAuthToken?device_id=Oarfs3DqKbfl5Z2fmXKekFyJnienvB1gnXph5GTxFn8%3D"

        payload = "cc=in&dolby_support=false&session_device_id=Oarfs3DqKbfl5Z2fmXKekFyJnienvB1gnXph5GTxFn8%253D.1705401009&app_version=9.11&_marker=0&ctx=android&tz=Asia%2FKolkata&source=app_launch&api_version=4&manufacturer=samsung&network_operator=JIO+4G&provider_state=checking&readable_version=9.11&build=UP1A.231005.007.S711BXXS2BWL4&v=390&_format=json&is_jio_user=true&model=SM-S711B&network_subtype=&state=login&network_type=WIFI\n"
        headers = {
            'accept-encoding': 'gzip',
            'connection': 'Keep-Alive',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'exp_details=%7B%22e583%22%3A%22D%22%2C%22e598%22%3A%22A%22%2C%22e606%22%3A%22C%22%2C%22e611%22%3A%22B%22%2C%22e620%22%3A%22HP-D%22%2C%22e624%22%3A%22A%22%2C%22e625%22%3A%22A100%22%2C%22e628%22%3A%22C%22%2C%22e630%22%3A%22C%22%2C%22e632%22%3A%22CON%22%7D; B=5e6d767427925d9ade47c3093dc8cfcc; device_id=Oarfs3DqKbfl5Z2fmXKekFyJnienvB1gnXph5GTxFn8%3D; CH=G03%2CA07%2CO00%2CL03; mm_latlong=19.0748%2C72.8856; DL=english; advertising_id=7554bcb0-24a7-481b-a1ac-7addfcc3907c; I=Jooja4un%2FLIhi7btO9%2FaYqDXBVz9M72CrQuPgZ4rLuoiGxtz4HzvNkh7s0XL2KeOepdJU%2F3u5mFzmx51qBQVIBQqD7LcJ22ZhDzSIsSwCWD5RqMucamq5bvIPcrzkmqyFNR4D9rOz2KzcqHOUYvJ%2Fi7InwhVCZRvykQPyfgzwfv0suycUP0jiJvGcLKAopDnWKPPRqFTjML1lXxPZmy07fbUa5ggE6g%2Fxgzo4NYfdSY%2B9oQ6I50Y0jLx%2B9lXKyIFN7MxupEt63JfraEj%2BFvuZ5ElM0nw8B5Noaht3R%2FZ88JpFk89U%2FvrHNiMGcYZchPCafKO2ohLUidpycCD0R%2FKK70HoI3jIlpKD0euts8drbKA3MSPuSJB%2FHkHuDOa%2BvFuQcwHZEEIkrs%3D; L=hindi,english; ssid=Oarfs3DqKbfl5Z2fmXKekFyJnienvB1gnXph5GTxFn8%3D.1705401009; network=apple; geo=182.48.212.43%2CIN%2CMaharashtra%2CMumbai%2C400070; P=expired%3A1683720598; CT=Mjk4MTM5MTQ5; client_sign=[VyO2swD3nSg]; SG=m; abpc=%7B%22ab_test%22%3A%7B%22splash%22%3A%22single_artist%22%2C%22paywall%22%3A%22phone_green%22%2C%22freemium%22%3A%22b%22%7D%2C%22first_seen_at%22%3A%2220240112%22%2C%22first_seen_at_ts%22%3A1705070096%7D; android_id=28e400cc066ce7d5',
            'host': 'drm-staging.saavn.com',
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 14; SM-S711B Build/UP1A.231005.007)'
        }
        response = self.client.post(url, headers=headers, data=payload)
        assert 'token' in response.text

    @task()
    def check_android_audio_license_001(self):
        url = "/getAudioAndroidLicense"

        # Specify the path to your file
        file_path = '8gyg6pEfruBYXKIR6AielyJnienvB1gnXph5GTxFn8=_uQQn_GHl.txt'

        # Read the contents of the file
        with open(file_path, 'rb') as file:
            file_contents = file.read()

        # Set headers as needed
        headers = {
            'accept-encoding': 'gzip',
            'connection': 'Keep-Alive',
            'content-type': 'application/octet-stream',
            'cookie': 'exp_details=%7B%22e583%22%3A%22D%22%2C%22e598%22%3A%22A%22%2C%22e606%22%3A%22C%22%2C%22e611%22'
                      '%3A%22B%22%2C%22e620%22%3A%22HP-D%22%2C%22e624%22%3A%22A%22%2C%22e625%22%3A%22A100%22%2C'
                      '%22e628%22%3A%22C%22%2C%22e630%22%3A%22C%22%2C%22e632%22%3A%22CON%22%7D; '
                      'B=5e6d767427925d9ade47c3093dc8cfcc; device_id=/8gyg6pEfruBYXKIR6AielyJnienvB1gnXph5GTxFn8%3D; '
                      'CH=G03%2CA07%2CO00%2CL03; mm_latlong=19.0748%2C72.8856; DL="english";$Domain=".saavn.com"; '
                      'advertising_id="7554bcb0-24a7-481b-a1ac-7addfcc3907c";$Path="/";$Domain=".saavn.com"; '
                      'I=Jooja4un%2FLIhi7btO9%2FaYqDXBVz9M72CrQuPgZ4rLuoiGxtz4HzvNkh7s0XL2KeOepdJU'
                      '%2F3u5mFzmx51qBQVIBQqD7LcJ22ZhDzSIsSwCWD5RqMucamq5bvIPcrzkmqyFNR4D9rOz2KzcqHOUYvJ'
                      '%2Fi7InwhVCZRvykQPyfgzwfv0suycUP0jiJvGcLKAopDnWKPPRqFTjML1lXxPZmy07fbUa5ggE6g%2Fxgzo4NYfdSY'
                      '%2B9oQ6I50Y0jLx%2B9lXKyIFN7MxupEt63JfraEj%2BFvuZ5ElM0nw8B5Noaht3R%2FZ88JpFk89U'
                      '%2FvrHNiMGcYZchPCafKO2ohLUidpycCD0R%2FKK70HoI3jIlpKD0euts8drbKA3MSPuSJB%2FHkHuDOa'
                      '%2BvFuQcwHZEEIkrs%3D; L="hindi,english";$Domain=".saavn.com"; '
                      'ssid="/8gyg6pEfruBYXKIR6AielyJnienvB1gnXph5GTxFn8=.xhckdsf";$Path="/";$Domain=".saavn.com"; '
                      'network=apple; geo=182.48.212.43%2CIN%2CMaharashtra%2CMumbai%2C400070; P=expired%3A1683720598; '
                      'CT=Mjk4MTM5MTQ5; client_sign="[VyO2swD3nSg]";$Path="/";$Domain=".saavn.com"; SG=m; '
                      'abpc=%7B%22ab_test%22%3A%7B%22splash%22%3A%22single_artist%22%2C%22paywall%22%3A%22phone_green'
                      '%22%2C%22freemium%22%3A%22b%22%7D%2C%22first_seen_at%22%3A%2220240112%22%2C%22first_seen_at_ts'
                      '%22%3A1705070096%7D; android_id="28e400cc066ce7d5";$Path="/";$Domain=".saavn.com"; '
                      'P=pro%3A1733211507; TID=anR1bmVfdGllcg%3D%3D%3A1733211507; '
                      'exp_details=%7B%22e583%22%3A%22A%22%2C%22e598%22%3A%22C%22%2C%22e606%22%3A%22B%22%2C%22e620%22'
                      '%3A%22HP-D%22%2C%22e628%22%3A%22B%22%2C%22e630%22%3A%22A%22%2C%22e632%22%3A%22CON%22%2C%22e633'
                      '%22%3A%22B%22%2C%22e634%22%3A%22C%22%7D; geo=103.195.202.70%2CIN%2CMaharashtra%2CBorivli%2C-; '
                      'mm_geo=103.195.202.70%2CIN%2CMaharashtra%2CMumbai%2C400079',  # Make sure 'cookie' is a
            # variable in your class containing the cookie value
            'host': 'drm-staging.saavn.com',
            'user-agent': 'com.jio.media.jiobeats/9.11 (Linux;Android 14) ExoPlayerLib/2.18.1',
        }

        # Make the POST request with the Locust client and the file contents in the data parameter
        response = self.client.post(url, headers=headers, data=file_contents)

        # Print or assert the response as needed
        assert response.status_code == 200

    # @task
    # def check_android_audio_license_004(self):
    #     url = "/getAudioAndroidLicense"
    #
    #     file_path = 'output_DRM-Oarfs3DqKbfl5Z2fmXKekFyJnienvB1gnXph5GTxFn8=_0Mfa6gsB.txt'
    #
    #     # Read the contents of the file
    #     with open(file_path, 'rb') as file:
    #         file_contents = file.read()
    #     headers = {
    #         'accept-encoding': 'gzip',
    #         'connection': 'Keep-Alive',
    #         'content-type': 'application/octet-stream',
    #         'cookie': 'exp_details=%7B%22e583%22%3A%22D%22%2C%22e598%22%3A%22A%22%2C%22e606%22%3A%22C%22%2C%22e611%22'
    #                   '%3A%22B%22%2C%22e620%22%3A%22HP-D%22%2C%22e624%22%3A%22A%22%2C%22e625%22%3A%22A100%22%2C'
    #                   '%22e628%22%3A%22C%22%2C%22e630%22%3A%22C%22%2C%22e632%22%3A%22CON%22%7D; '
    #                   'B=5e6d767427925d9ade47c3093dc8cfcc; device_id=Oarfs3DqKbfl5Z2fmXKekFyJnienvB1gnXph5GTxFn8%3D; '
    #                   'CH=G03%2CA07%2CO00%2CL03; mm_latlong=19.0748%2C72.8856; DL="english";$Domain=".saavn.com"; '
    #                   'advertising_id="7554bcb0-24a7-481b-a1ac-7addfcc3907c";$Path="/";$Domain=".saavn.com"; '
    #                   'I=Jooja4un%2FLIhi7btO9%2FaYqDXBVz9M72CrQuPgZ4rLuoiGxtz4HzvNkh7s0XL2KeOepdJU'
    #                   '%2F3u5mFzmx51qBQVIBQqD7LcJ22ZhDzSIsSwCWD5RqMucamq5bvIPcrzkmqyFNR4D9rOz2KzcqHOUYvJ'
    #                   '%2Fi7InwhVCZRvykQPyfgzwfv0suycUP0jiJvGcLKAopDnWKPPRqFTjML1lXxPZmy07fbUa5ggE6g%2Fxgzo4NYfdSY'
    #                   '%2B9oQ6I50Y0jLx%2B9lXKyIFN7MxupEt63JfraEj%2BFvuZ5ElM0nw8B5Noaht3R%2FZ88JpFk89U'
    #                   '%2FvrHNiMGcYZchPCafKO2ohLUidpycCD0R%2FKK70HoI3jIlpKD0euts8drbKA3MSPuSJB%2FHkHuDOa'
    #                   '%2BvFuQcwHZEEIkrs%3D; L="hindi,english";$Domain=".saavn.com"; '
    #                   'ssid="1kAUfqJ2atMhny4nirPcIFyJnienvB1gnXph5GTxFn8=.xhckdsf";$Path="/";$Domain=".saavn.com"; '
    #                   'network=apple; geo=182.48.212.43%2CIN%2CMaharashtra%2CMumbai%2C400070; P=expired%3A1683720598; '
    #                   'CT=Mjk4MTM5MTQ5; client_sign="[VyO2swD3nSg]";$Path="/";$Domain=".saavn.com"; SG=m; '
    #                   'abpc=%7B%22ab_test%22%3A%7B%22splash%22%3A%22single_artist%22%2C%22paywall%22%3A%22phone_green'
    #                   '%22%2C%22freemium%22%3A%22b%22%7D%2C%22first_seen_at%22%3A%2220240112%22%2C%22first_seen_at_ts'
    #                   '%22%3A1705070096%7D; android_id="28e400cc066ce7d5";$Path="/";$Domain=".saavn.com"; '
    #                   'P=pro%3A1733211507; TID=anR1bmVfdGllcg%3D%3D%3A1733211507; '
    #                   'exp_details=%7B%22e583%22%3A%22A%22%2C%22e598%22%3A%22C%22%2C%22e606%22%3A%22B%22%2C%22e620%22'
    #                   '%3A%22HP-D%22%2C%22e628%22%3A%22B%22%2C%22e630%22%3A%22A%22%2C%22e632%22%3A%22CON%22%2C%22e633'
    #                   '%22%3A%22B%22%2C%22e634%22%3A%22C%22%7D; geo=103.195.202.70%2CIN%2CMaharashtra%2CBorivli%2C-; '
    #                   'mm_geo=103.195.202.70%2CIN%2CMaharashtra%2CMumbai%2C400079',
    #         'host': 'drm-staging.saavn.com',
    #         'user-agent': 'com.jio.media.jiobeats/9.11 (Linux;Android 14) ExoPlayerLib/2.18.1'
    #     }
    #
    #     response = self.client.post(url, headers=headers, data=file_contents)
    #     assert response.status_code == 200
