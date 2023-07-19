import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { UserInfo1 } from './type';


/**
 * 获取指定的用户信息
 * @param uid 用户id
 * @returns
 */
export function getUserInfo1Api(api_version:string,uid: number,query_params:Object): AxiosPromise {
  return request({
    url: '/'+api_version+'/users/'+uid,
    method: 'get',
    params:query_params
  });
}













