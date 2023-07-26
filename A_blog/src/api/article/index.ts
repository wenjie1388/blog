import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { ArticleListT } from './type';

/**
 * 获取文章列表
 * @param apiVersion 
 * @param quer_params 
 * @returns 
 */
export function getArticleListApi(apiVersion:string,quer_params:object): AxiosPromise<ArticleListT> {
  return request({
    url: '/'+ apiVersion+'/articles',
    method: 'get',
    params:quer_params
  });
}

/**
 * 添加文章
 * @param apiVersion 
 * @param body_data 
 * @returns 
 */
export function createArticleApi(apiVersion:string,body_data:object): AxiosPromise {
  return request({
    url: '/'+ apiVersion+'/articles',
    method: 'post',
    data:body_data
  });
}



/**
 * 获取文章信息
 * @param apiVersion 
 * @param aid 
 * @param quer_params 
 * @returns 
 */
export function getArticleInfoApi(apiVersion:string,aid:number,quer_params:object): AxiosPromise {
  return request({
    url: '/'+ apiVersion+'/articles/'+aid,
    method: 'get',
    params:quer_params
  });
}

/**
 * 更新文章
 * @param apiVersion 
 * @param aid
 * @param body_data 
 * @returns 
 */
export function patchArticleApi(apiVersion: string,aid:number, body_data: object): AxiosPromise {
  return request({
    url: '/'+ apiVersion+'/articles/'+aid,
    method: 'patch',
    data:body_data
  });
}

/**
 * 删除文章
 * @param apiVersion 
 * @param aid 
 * @returns 
 */
export function deleteArticleApi(apiVersion:string,aid:number): AxiosPromise {
  return request({
    url: '/'+ apiVersion+'/articles/'+aid,
    method: 'delete',
  });
}







