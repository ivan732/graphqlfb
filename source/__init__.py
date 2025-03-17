import requests, base64, json, re, time
from .utils import payload, convert_react_type

save = lambda x: open('/sdcard/Cache/x.htm', 'w').write(str(x))

class Facebook:
    def __init__(self, cookies: str) -> None:
        self.__cookies = cookies 
        self.__session = requests.session()

        self.base = 'https://web.facebook.com/'
        self.login_status = self.__check_cookies()

    def __check_cookies(self) -> bool:
        self.__session.cookies['cookie'] = self.__cookies
        source = self.__session.get(self.base)
        
        account_data = re.search(r'"USER_ID":"(\d+)","NAME":"(.*?)"', source.text)
        setattr(self, 'name', account_data.group(1))
        setattr(self, 'user_id', account_data.group(2))

        if 'logoutToken' in source.text: return True 
        return False 

    def post_reaction(self, post_id: str, reaction_type: str = 'angry') -> dict:
        reaction_id = convert_react_type(reaction_type=reaction_type.lower())
        feedback_id = base64.b64encode(('feedback:' + post_id).encode()).decode()
        
        source = self.__session.get(self.base).text
        data = payload(source=source)

        variables = {"input":{"attribution_id_v2":"CometHomeRoot.react,comet.home,via_cold_start,1742205175612,998424,4748854339,,","feedback_id": feedback_id,"feedback_reaction_id":reaction_id,"feedback_source":"NEWS_FEED","is_tracking_encrypted":True,"tracking":[None],"session_id":"","actor_id":data['__user'],"client_mutation_id":"1"},"useDefaultActor":False,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False}
        data.update({
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
            'variables': json.dumps(variables),
            'server_timestamps': 'true',
            'doc_id': '9232085126871383',
        })
        response = self.__session.post(self.base +'/api/graphql', data=data).text 
        if 'viewer_actor' in response:
            actor = re.search(r'"viewer_actor":\{"__typename":"User","id":"(\d+)","name":"(.*?)"\}', response)
            return {
                'success': True,
                'post': {
                    'reaction_count': re.search(r'"reaction_count":\{"count":(.*?)\}', response).group(1),
                    'reaction_type': reaction_type.capitalize(),
                    'reaction_id': reaction_id,
                    'url': self.base + post_id
                },
                'account': {
                    'name': actor.group(2),
                    'user_id': actor.group(1),
                }
            }

        else:
            return {
                'success': False,
                'post': {
                    'reaction_count': None,
                    'reaction_type': reaction_type.capitalize(),
                    'reaction_id': reaction_id,
                    'url': self.base + post_id
                },
                'account': {
                    'name': None,
                    'user_id': data['__user']
                }
            }

    def scrape_post_timeline(self) -> dict:
        source = self.__session.get(self.base).text
        data = payload(source=source)

        variables = {"RELAY_INCREMENTAL_DELIVERY":True,"clientQueryId":"","clientSession":None,"connectionClass":"EXCELLENT","count":5,"cursor":"","experimentalValues":None,"feedLocation":"NEWSFEED","feedStyle":"DEFAULT","feedbackSource":1,"focusCommentID":None,"orderby":["TOP_STORIES"],"privacySelectorRenderLocation":"COMET_STREAM","recentVPVs":[{"client_vpv_token":"","evt":"vpv","feed_backend_data_serialized_payloads":"","fetch_tracking":False,"original_qid":"-180207549591297281","qid":"-180207549591297281","timestamp":int(time.time() *1000),"vsid":"-4706000292813323956","vspos":2},{"client_vpv_token":"","evt":"vpv","feed_backend_data_serialized_payloads":"","fetch_tracking":False,"original_qid":"-180207549591297281","qid":"-180207549591297281","timestamp":int(time.time() *1000),"vsid":"-8951896928395739028","vspos":1},{"client_vpv_token":"","evt":"vpv","feed_backend_data_serialized_payloads":"","fetch_tracking":False,"original_qid":"-180207549591297281","qid":"-180207549591297281","timestamp":int(time.time() *1000),"vsid":"7211511239826767184","vspos":3},{"client_vpv_token":"","evt":"vpv","feed_backend_data_serialized_payloads":"","fetch_tracking":False,"original_qid":"-180207549591297281","qid":"-180207549591297281","timestamp":int(time.time() *1000),"vsid":"-7690355884901037852","vspos":4}],"refreshMode":"COLD_START","renderLocation":"homepage_stream","scale":3,"shouldChangeBRSLabelFieldName":False,"shouldChangeSponsoredAuctionDistanceFieldName":False,"shouldChangeSponsoredDataFieldName":False,"shouldObfuscateCategoryField":False,"useDefaultActor":False,"__relay_internal__pv__GHLShouldChangeSponsoredAuctionDistanceFieldNamerelayprovider":False,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":False,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":False,"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__FBReels_deprecate_short_form_video_context_gkrelayprovider":False,"__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider":500,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":False,"__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":True,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":True,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":True,"__relay_internal__pv__FBReelsIFUTileContent_reelsIFUPlayOnHoverrelayprovider":False,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":True}
        data.update({
            'qpl_active_flow_ids': '29822561',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometNewsFeedPaginationQuery',
            'variables': json.dumps(variables),
            'server_timestamps': 'true',
            'doc_id': '9460305997388636',
        })

        response = self.__session.post(self.base +'/api/graphql', data=data).text
        if 'ORGANIC' in response:
            result = {'success': True, 'data': []}
            query = re.findall(r'"post_id":"(\d+)","actors":\[\{"__typename":"User","id":"(\d+)","name":"(.*?)","__isEntity":"User","url":"(.*?)"\}\],"message":\{"__typename":"TextWithEntities","text":"(.*?)"', response)

            for data in query:
                result['data'].append({
                    'post': {
                        'id': data[0],
                        'url': data[3],
                        'caption': data[4]
                    },
                    'publisher': {
                        'user_id': data[1],
                        'name': data[2]
                    }
                })
        else:
            result = {'success': False, 'data': []}

        return result



if __name__ == "__main__":
    cookies = 'dbln=%7B%22100000615216344%22%3A%229bSQzZYx%22%7D; datr=ZmWrZ5zJafE99nOsc-zEKgL9; sb=ZmWrZ1hTf5Os7BDUSVMOcS0i; ps_l=1; ps_n=1; dpr=2.1988937854766846; wd=891x1718; locale=id_ID; c_user=100000615216344; xs=46%3A6iaqPNAvnr94Nw%3A2%3A1742134099%3A-1%3A11186; fr=0Nqbptof04SHvb3gw.AWU5HTOPNwHetc44Mqhx6OCsyOBmBMORCTIM1g.Bnq2Vm..AAA.0.0.Bn1ttW.AWVaHcvtWls; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1742134120743%2C%22v%22%3A1%7D; ar_debug=1'
    print(Facebook(cookies=cookies).scrape_post_timeline())
