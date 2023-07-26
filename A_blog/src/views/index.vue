<template>
  <el-row :gutter="14">
    <el-col :span="12" :offset="2">
      <OneVue v-for="item in articles_list.results" :key="item.id" :article="item" />
    </el-col>
    <el-col :span="6" style="padding-top: 5px">
      <el-card :body-style="{ padding: '0px' }">
        <el-avatar :size="size" src="" />
        <div style="padding: 14px">
          <span>{{ user.username }}</span>
          <div class="bottom">
            <time class="time">{{ user.email }}</time>
            <el-button text class="button">Operating</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
// 系统依赖
import { ref, onMounted, onUpdated, reactive } from "vue";
import { RouterLink, RouterView } from "vue-router";

// Api 依赖
import { getUserInfoApi } from "@/api/user";
import { getArticleListApi } from "@/api/article";
import { ArticleListT, ArticleList } from "@/api/article/type";
var articles_list = ref<ArticleListT>({
  count: 0,
  next: "",
  previous: "",
  results: [],
});

var user = reactive({
  username: "",
  email: "",
  avater: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
});

const size = ref("large");

async function InitUser() {
  const params = { username: "", email: "", avater: "" };
  getUserInfoApi("v1", 4, params).then((res) => {
    const data = res.data;
    user.username = data.username;
    user.email = data.email;
    user.avater = data.avater;
  });
}

async function InitArticles() {
  const params = { search: "", status: "or", order1: "" };
  getArticleListApi("v1", params).then((res) => {
    // console.log(res.data)
    articles_list.value = res.data;
    console.log(articles_list.value);
    // article = articles.results
  });
}

onMounted(() => {
  InitUser();
  InitArticles();
});
</script>

<style scoped></style>
