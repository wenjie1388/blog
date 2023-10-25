<template>
  <div class="up-container" style="">
    <!-- <el-row>
      <el-col :span="16" :offset="4" style="" class="WC-container">
        <div class="WJsBlog"><span> WJ's Blog</span></div>
        <div><span class="wellcome">欢迎参观我的博客 \(^Д^*)/</span></div>
      </el-col>
    </el-row> -->

    <!-- <el-row>
      <el-col :span="16" :offset="4" style="" class="">
        <el-carousel indicator-position="outside">
          <el-carousel-item v-for="item in 4" :key="item" style="background-color: blanchedalmond">
            <el-row :gutter="20">
              <el-col :span="6">
                <div class="title">
                  Blog post title goes here ipsum dolor sit amet, consectetur
                </div>
                <div class="edi">20 December 2018 by Mikolaj Dobrucki</div>
                <div class="com-tags">学习笔记</div>
              </el-col>
              <el-col :span="6">
                <el-image style="width: 640px; height: 500px"
                  src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg" fit="contain" />
              </el-col>
            </el-row>
          </el-carousel-item>
        </el-carousel>
      </el-col>
    </el-row> -->
  </div>

  <el-row class="">
    <!-- 我的文章 -->
    <el-col :span="11" :offset="4" style="" class="">
      <el-row :gutter="1" class="con-articlecard">
        <el-col :span="8">
          <el-image style="width: 210px; height: 145px" src="https://img.js.design/assets/smartFill/img419164da758808.jpg"
            fit="contain" />
        </el-col>
        <el-col :span="14">
          <div class="con-title">长在火山泥里的夏威夷果，不用剥壳好好吃。</div>
          <div class="con-tags"></div>
          <div class="con-abstra">
            口味不错，4人餐足够吃，服务也很周到耐心。但是速度有些慢了，总体还不错。
          </div>
          <div class="con-info"></div>
        </el-col>
      </el-row>
    </el-col>

    <!-- 我的卡片 -->
    <el-col class="con-usercard" :span="4" :offset="1" style="">
      <el-col class="con-item avatar">
        <el-avatar :size="120" :src="user.avater" @error="errorHandler">
          <img src="https://img.js.design/assets/smartFill/img340164da748e08.jpg" />
        </el-avatar>
      </el-col>
      <el-col class="con-item name">{{ user.username }}</el-col>
      <el-col class="con-item abstr text-type1"><span>{{ user.abstract }}</span></el-col>
      <el-col class="con-item tot">
        <div class="con-item">
          <text class="text-type1">文章</text>
          <h3>135</h3>
        </div>
        <div class="con-item">
          <text class="text-type1">阅读</text>
          <h3>135</h3>
        </div>
        <div class="con-item">
          <text class="text-type1">点赞</text>
          <h3>135</h3>
        </div>
        <div class="con-item">
          <text class="text-type1">评论</text>
          <h3>135</h3>
        </div>
      </el-col>
      <el-col class="con-item ltype">
        <el-tooltip v-if="user.email != ''" :content="user.email" popper-class=".ltype-item" :show-arrow="false"
          :offset="5">
          <svg t="1695405015802" class="icon" viewBox="0 0 1365 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
            p-id="1511" width="30">
            <path
              d="M1365.203314 853.252071a168.115037 168.115037 0 0 1-22.135797 81.814685L911.955814 453.052471 1338.581849 82.009713a169.285211 169.285211 0 0 1 26.621465 90.493477v680.553852zM682.601657 540.718027L1275.587468 21.258166a167.627464 167.627464 0 0 0-81.814684-21.258166H169.967813A168.992667 168.992667 0 0 0 87.76307 21.258166z m163.824398-31.887249L709.223122 629.553757a40.858585 40.858585 0 0 1-56.070851 0L515.851824 508.830778l-434.03714 488.547757a168.212551 168.212551 0 0 0 90.103419 26.231407h1023.902486a168.212551 168.212551 0 0 0 90.103418-26.231407L848.376345 508.830778h-1.95029zM26.621465 82.009713A169.967813 169.967813 0 0 0 0 170.942958v682.601657a167.724979 167.724979 0 0 0 22.135797 81.814684l430.81916-482.014284L26.718979 82.78983z m0 0z"
              fill="#999999" p-id="1512"></path>
          </svg>
        </el-tooltip>
      </el-col>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
// 系统依赖
import { ref, onMounted, onUpdated, reactive, useSSRContext } from "vue";
import { RouterLink, RouterView } from "vue-router";

// Api 依赖
import { getUserInfoApi } from "@/api/user";
import { getArticleListApi } from "@/api/article";
import { ArticleListT, ArticleList } from "@/api/article/type";

const errorHandler = () => true;
const size = ref("large");

var user = reactive({
  username: "",
  email: "",
  avater: "",
  abstract: "",
});

var articles_list = ref<ArticleListT>({
  count: 0,
  next: "",
  previous: "",
  results: [],
});

async function InitUser() {
  // const params = { username: "", email: "" };
  getUserInfoApi("2").then((res) => {
    const data = res.data;
    console.log(data.email);

    user.username = data.username;
    user.email = data.email;
    user.avater = data.avater;
    user.abstract = data.abstract;
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

<style scoped lang="scss">
.text-type1 {
  /** 文本1 */
  font-size: 15px;
  font-weight: 500;
  letter-spacing: 0px;
  line-height: 20.58px;
  color: rgba(138, 138, 138, 1);
  text-align: center;
  vertical-align: top;
}

.up-container {
  background-image: url("@/assets/background1.png");
  margin: 0 auto;
  padding: 0;
  background-size: contain;
  width: 100%;
}

.WC-container {
  left: 621px;
  top: 99px;
  width: 679px;
  height: 186px;
  opacity: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;

  .WJsBlog {
    left: 0px;
    top: 0px;
    width: 602px;
    height: 97px;
    opacity: 1;
    text-shadow: 0px 10px 10px rgba(0, 0, 0, 1);
    display: flex;
    margin: 0 auto;

    /** 文本1 */
    font-size: 70px;
    font-weight: 900;
    letter-spacing: 0px;
    line-height: 96.04px;
    color: rgba(255, 255, 255, 1);
    text-align: center;
    vertical-align: top;
  }

  .wellcome {
    left: 0px;
    top: 117px;
    width: 679px;
    height: 69px;
    opacity: 1;
    text-shadow: 0px 10px 10px rgba(0, 0, 0, 0.75);
    display: flex;
    margin: 0 auto;

    /** 文本1 */
    font-size: 50px;
    font-weight: 500;
    letter-spacing: 0px;
    line-height: 68.6px;
    color: rgba(255, 255, 255, 1);
    text-align: left;
    vertical-align: top;
  }
}

.con-articlecard {
  border-radius: 15px;
  background: rgba(250, 250, 250, 1);
  box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
}

.con-usercard {
  border-radius: 15px;
  background: rgba(250, 250, 250, 1);
  box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.5);
  margin-top: 70px;
  margin-bottom: 20px;
  padding: 30px 20px 30px 20px;

  .con-item {
    display: flex;
    justify-content: center;
    margin-top: 10px;
    margin-bottom: 10px;
  }

  .name {
    /** 文本 */
    font-size: 30px;
    font-weight: 500;
    letter-spacing: 0px;
    line-height: 41.16px;
    color: rgba(56, 56, 56, 1);
    text-align: center;
    vertical-align: top;
  }

  .abstr {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    // 文本
    // font-size: 15px;
    // font-weight: 500;
    // letter-spacing: 0px;
    // line-height: 20.58px;
    // color: rgba(138, 138, 138, 1);
    // text-align: center;
    // vertical-align: top;
  }

  .tot {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;

    .con-item {
      display: flex;
      flex-direction: column;
    }
  }

  .ltype {
    .ltype-item:hover {
      cursor: pointer;
    }

    .ltype-item {
      display: flex;
    }
  }
}
</style>
