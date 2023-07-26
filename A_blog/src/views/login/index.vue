<template>
  <div>登录</div>
</template>

<script setup lang="ts">
// 页面依赖
import { reactive, ref, toRefs } from "vue";
import type { FormInstance, FormRules, FormValidateCallback } from "element-plus";
import { ElMessage } from "element-plus";

// 状态管理依赖
import { useUserStore } from "@/stores/modules/user";
const userStore = useUserStore();

// API依赖
import { LocationQuery, LocationQueryValue, useRoute } from "vue-router";

// 倒计时时长
const time60s = ref(60);

/**
 * 按钮loading
 */
const loading = ref(false);

/**
 * 是否大写锁定
 */
const isCapslock = ref(false);

/**
 * 密码是否可见
 */
const passwordVisible = ref(false);
/**
 * 按钮是否禁用
 */
const isdisabled = ref(false);
/**
 * 是否隐藏*号标记
 */
const isasterisk = ref(true);

// const route = useRoute();
const loginRef = ref<FormInstance>();
const loginData = reactive({
  username: "",
  password: "",
});
const captcha = ref();

const loginRules = ref<FormRules>({
  username: [
    { required: true, message: "账号不能空", trigger: "change" },
    { min: 6, max: 24, message: "长度在6-24之间", trigger: "change" },
  ],
  password: [
    { required: true, message: "密码不能空", trigger: "change" },
    { min: 8, max: 24, message: "长度在8-24之间", trigger: "change" },
  ],
});

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  await formEl.validate((valid, fields) => {
    if (valid) {
      // 验证码校验
      // if (captcha.value === userStore.captcha) {
      //   loading.value = true;
      //   userStore
      //     .login("010203", loginData)
      //     .then(() => {
      //       router.push("/");
      //     })
      //     .catch(() => {
      //       ElMessage.warning("用户名或密码错误");
      //       loading.value = false;
      //     })
      //     .finally(() => {
      //       loading.value = false;
      //     });
      // } else {
      //   ElMessage.warning("验证码错误");
      // }
    } else {
      isasterisk.value = false;
    }
  });
};

const sendCode = async (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  await formEl.validate((valid, fields) => {
    if (valid) {
      isdisabled.value = true;
      // userStore(loginData.username).then(() => {
      // 倒计时
      const timer = setInterval(() => {
        //   time60s.value -= 1;
        //   if (time60s.value == 0) {
        //     isdisabled.value = false;
        //     time60s.value = 60;
        //     clearTimeout(timer);
        //   }
        // }, 1000);
      });
    }
  });
};
</script>

<style scoped lang="scss">
.inputCode-con {
  width: 80px;
  margin-right: 20px;
}
</style>
