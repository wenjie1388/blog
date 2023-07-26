// 系统依赖
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

// utils/auth
import {
  getToken, setToken, removeToken, setId, getId, removeId
} from '@/utils/auth'

// user API
import {
  loginApi,
  getUserInfoApi,
  updateUserInfoApi,
  deleteUserApi,
} from '@/api/user'


export const useUserStore = defineStore('user', () => {
  // state
  
  // 登录信息
  const id = ref<number>(0)
  const username = ref<string>('')
  const avatar = ref<string>('') // 用户头像
  const token = ref<string>(getToken() || '')  
  
  // 用户资料 02
  const male = ref<string>('') // 性别
  const introduction = ref<string>('')
  const address = ref<string>('')

  // 账号信息 03
  const password = ref<string>('') // 密码
  const cellphone = ref<string>('') // 手机
  const email = ref<string>('') // 邮箱
  const lastLogin = ref<string>('')
  const joinDate = ref<string>('')

  // 权限信息 04
  const active = ref<boolean>(false) // True-账号已激活，能登录；反之则不能登录
  const status = ref<boolean>(false) // true=重新登录
  const auth= ref<boolean>(false) 
  
  // 认证信息 05
  const name = ref<string>('') // 姓名
  const idCard= ref<string>('')  // 身份证号

  // actions
  /**
   * 1、用户登录
   * @param apiVersion 
   * @param loginForm 
   * @returns 
   */
  function login(loginForm,apiVersion) {
    return new Promise<void>((resolve, reject) => {
      loginApi(loginForm,apiVersion)
        .then((data) => {
          id.value = data.id
          token.value ="Bearer "+ data.token // Bearer eyJhbGciOiJIUzI1NiJ9.xxx.xxx
          username.value =data.username
          avatar.value = data.avatar
          setToken(token.value)
          resolve()
        })
        .catch(error => {
          reject(error)
        })
    })
  }

  /**
   * 2、获取用户信息
   * @param apiVersion 
   * @param actionEncode 
   * @returns 
   */
  function getInfo(uID,actionEncode:string,apiVersion:string) {
    return new Promise<void>((resolve, reject) => {
      getUserInfoApi(uID,'0103'+actionEncode,apiVersion)
        .then((data) => {
          if (actionEncode == '02') {
            male.value = data.male
            introduction.value = data.introduction
            address.value = data.address  
          }else if(actionEncode == '03') { 
            password.value = data.password
            cellphone.value = data.cellphone
            email.value = data.email  
            lastLogin.value = data.lastLogin
            joinDate.value = data.joinDate
          }else if(actionEncode == '04') { 
            active.value = data.is_activate
            auth.value = data.auth
            status.value = data.status
          }else if(actionEncode == '05'){
            name.value = data.name
            idCard.value = data.idCard
          } else {
            ElMessage.error("actionEncode:"+actionEncode+' 错误！')  
          }
          resolve(data)
        })
        .catch(error => {
          reject(error)
        })
    })
  }

  /**
   * 3、更新用户信息 04
   * @param UpdateForm 更新表单
   * @returns 
   */
  function updateInfo(ActionEncode,UpdateForm:object) { 
    return new Promise<void>((resolve, reject) => {
      updateUserInfoApi(id.value,'0104'+ActionEncode,UpdateForm)
        .then((data) => {
          getUserInfoApi(id.value,ActionEncode)
          resolve()
        })
        .catch((error) => { 
          reject(error)
        })
    })
  }

  /**
   * 4、登出
   * @returns 
   */
  function logout() {
    return new Promise<void>((resolve, reject) => {
      logoutApi(id.value)
        .then(() => {
          resetRouter()
          resetUser()
          resolve()
        })
        .catch(error => {
          reject(error)
        })
    })
  }
  return {
    id,
    username,
    avatar,
    token,

    male,
    introduction,
    address,

    // 账号信息 
    password,
    cellphone,
    email,
    lastLogin,
    joinDate,

    active,
    status,
    auth,

    name,
    idCard,

    login,
    logout,
    getInfo,
    updateInfo,
  }
})

// // 非setup
// export function useUserStoreHook() {
//   return useUserStore(store)
// }
