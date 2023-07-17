import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { ArticleListT } from './type';


/**
 * 获取文章信息
 * @param 
 * @returns
 */
export function getArticleApi(apiVersion:string,quer_params:object): AxiosPromise<ArticleListT> {
  return request({
    url: '/'+ apiVersion+'/articles',
    method: 'get',
    params:quer_params
  });
}













