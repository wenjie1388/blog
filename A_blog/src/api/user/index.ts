import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { UserInfo1 } from './type';


/**
 * 获取所有用户
 * @param api_version 
 * @returns 
 */
export function getUserApi(api_version:string): AxiosPromise {
  return request({
    url: '/users/',
    method: 'get',
  });
}

/**
 * 获取指定用户信息
 * @param uid 
 * @returns 
 */
export function getUserInfoApi(uid:string): AxiosPromise {
  return request({
    url: '/users/'+uid,
    method: 'get',
  });
}












