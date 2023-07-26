import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { UserInfo1 } from './type';

/**
 * 用户登录
 * @param api_version 
 * @param query_params 
 * @returns 
 */
export function LoginApi(api_version:string,query_params:Object): AxiosPromise {
  return request({
    url: '/'+api_version+'/login',
    method: 'get',
    params:query_params
  });
}

/**
 * 退出登录
 * @param api_version 
 * @param uid 
 * @returns 
 */
export function logoutApi(api_version:string,uid: number): AxiosPromise {
  return request({
    url: '/'+api_version+'/users/'+uid,
    method: 'get',
  });
}



/**
 * 获取用户列表
 * @param api_version 
 * @param uid 
 * @param query_params 
 * @returns 
 */
export function getUserListApi(api_version:string,uid:number,query_params:Object): AxiosPromise {
  return request({
    url: '/'+api_version+'/users/'+uid,
    method: 'get',
    params:query_params
  });
}




/**
 * 用户注册
 * @param api_version 
 * @param body_data 
 * @returns 
 */
export function RegisterApi(api_version:string,body_data:Object): AxiosPromise {
  return request({
    url: '/'+api_version+'/users',
    method: 'post',
    data:query_params
  });
}

/**
 * 获取指定的用户信息
 * @param uid 用户id
 * @returns
 */
export function getUserInfoApi(api_version:string,uid: number,query_params:Object): AxiosPromise {
  return request({
    url: '/'+api_version+'/users/'+uid,
    method: 'get',
    params:query_params
  });
}


/**
 * 更新用户信息
 * @param api_version 
 * @param uid 
 * @param body_data 
 * @returns 
 */
export function patchUserInfoApi(api_version:string,uid: number,body_data:Object): AxiosPromise {
  return request({
    url: '/'+api_version+'/users/'+uid,
    method: 'patch',
    data:body_data
  });
}



/**
 * 删除用户
 * @param api_version 
 * @param uid 
 * @returns 
 */
export function deleteUserApi(api_version:string,uid: number): AxiosPromise {
  return request({
    url: '/'+api_version+'/users/'+uid,
    method: 'delete',
  });
}








