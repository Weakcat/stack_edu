<template>
    <div>
        <van-cell-group>
            <van-cell 
            v-for = "quiz in quizzes" 
            :key = "quiz.id" 
            :title="quiz.name" 
            :label="quiz.time"
            is-link 
            value="内容"
            to="/quiz"/>
        </van-cell-group>
        <van-swipe-cell>
        <template #left>
            <van-button square type="primary" text="选择" />
        </template>
        <van-cell :border="false" title="单元格" value="内容" />
        <template #right>
            <van-button square type="danger" text="删除" />
            <van-button square type="primary" text="收藏" />
        </template>
        </van-swipe-cell>
        

    </div>
</template>

<script>
import { Cell, CellGroup,SwipeCell } from 'vant';
import axios from 'axios';
import '@vant/touch-emulator';


export default {
    name: 'APP',
    components: {
        [Cell.name]: Cell,
        [CellGroup.name]: CellGroup,
        [SwipeCell.name]:SwipeCell,
    },
    data: function() {
        return{ 
            quizzes : [],
        }
    },
    async mounted(){
        let next_resp = await axios.get('http://localhost:5000/v1/quizzes', {headers:{
            'Authorization':localStorage.getItem('accessToken')}
            }
        );
        this.quizzes = next_resp.data.quiz
        console.log(next_resp.data)

    },
    methods: {

    }
}

</script>