<template>
    <div>
        <van-form @submit="onSubmit">
        <van-field
            v-model="username"
            name="用户名"
            label="用户名"
            placeholder="用户名"
            :rules="[{ required: true, message: '请填写用户名' }]"
        />
        <van-field
            v-model="password"
            type="password"
            name="密码"
            label="密码"
            placeholder="密码"
            :rules="[{ required: true, message: '请填写密码' }]"
        />
        <div style="margin: 16px;">
            <van-button round block type="info" native-type="submit">
            提交
            </van-button>
        </div>
        </van-form>
    </div>
</template>

<script>
import { Button, Field, Form, Toast} from 'vant';
import axios from 'axios';

export default {
    name: 'APP',
    components: {
        [Button.name]: Button,
        [Field.name]: Field,
        [Form.name]: Form,
        [Toast.name]: Toast,
    },
    data: function() {
        return{ 
            username: '',
            password: ''
        }
    },
    async mounted(){

    },
    methods: {
        async onSubmit(values){
            try {
                let resp = await axios.post('http://localhost:5000/auth', {
                    username: this.username,
                    password: this.password,
                });
                console.log(resp.data)
                localStorage.setItem('accessToken', 'JWT '+resp.data.access_token)                 
                console.log(localStorage.getItem('accessToken'))

                console.log('submit',values);
                let next_resp = await axios.get('http://localhost:5000/v1/quizzes', {headers:{
                    'Authorization':localStorage.getItem('accessToken')}
                    }
                );
                Toast(JSON.stringify(next_resp.data))
                console.log(next_resp)
                this.$router.push('/quizzes').catch(() =>{
                    console.log('页面跳转失败');
                });

            } catch(e) {
                console.log('收不到token');
                Toast(e.response.data.description);
            }

            
        }
    }
}

</script>