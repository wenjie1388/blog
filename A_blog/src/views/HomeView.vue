

<template>
  <main>
    <OneVue v-for="item in articles.results" :key="item.id" :article="item" />
    <el-pagination background layout="prev, pager, next" :total="articles.count" />
  </main>
</template>
<script setup lang="ts">

import { onMounted, reactive, ref } from 'vue';
import { getArticleApi } from "@/api/article";
import { ArticleListT, ArticleList } from '@/api/article/type';
import OneVue from '@/components/article_guide/One.vue';


var articles = ref<ArticleListT>({
  count: 0,
  next: '',
  previous: '',
  results: []
})

async function InitArticle() {
  getArticleApi('v1', { "search": "", "status": 'or', "order1": '' })
    .then((res) => {
      // console.log(res.data)
      articles.value = res.data
      // article = articles.results
    })

}

onMounted(() => {
  InitArticle();
})



</script>


<style lang="scss" scoped></style>