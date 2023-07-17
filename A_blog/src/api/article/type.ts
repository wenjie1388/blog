/**
 * 获取文章列表
 */
export interface ArticleListT {
    count: number;
    next: string;
    previous: string;
    results: ArticleList[];
}

export interface ArticleList {
    author: string;
    body: string;
    collect: number;
    cover: string;
    date_create: string;
    date_update: string;
    digest: string;
    id: number;
    pageviews: number;
    status: string;
    tags: string;
    title: string;
    upvote: number;
}
