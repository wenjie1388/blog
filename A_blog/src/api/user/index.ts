import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { UserInfo1 } from './type';


/**
 * 获取指定用户信息1
 * @param UId 用户id
 * @returns
 */
export function getUserInfo1Api(UId: number): AxiosPromise<UserInfo1> {
  return request({
    url: 'v1/users/'+UId,
    method: 'get',
  });
}













