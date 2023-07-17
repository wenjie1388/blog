<template>
  <div>
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>{{ article?.title }}</span>
          <el-button class="button" text>查看详情</el-button>
        </div>
      </template>
      <div key="" class="text item">{{ article?.body }}</div>
    </el-card>
  </div>
</template>


<script setup lang="ts" >
import { reactive, toRef } from 'vue';
// import { ArticleList } from '@/api/article/type';
const props = defineProps({
  // article: Object,
  article: Object,
  msg: String,

})


// const {} = toRef(props);

// console.log(article)
</script>


<style scoped></style>
