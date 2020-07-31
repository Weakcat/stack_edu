<template>
    <div>
        <van-cell-group>
            <van-cell 
            v-for = "question in questions" 
            :key = "question.id" 
            :title="question.order" 
            :label="question.answer"
            is-link 
            :value="question.answer"
            to="/"/>
        </van-cell-group>
    </div>
</template>

<script>
import { Cell, CellGroup } from 'vant';
import axios from 'axios';

export default {
    name: 'APP',
    components: {
        [Cell.name]: Cell,
        [CellGroup.name]: CellGroup,
    },
    data: function() {
        return{ 
            questions : [],
        }
    },
    async mounted(){
        let next_resp = await axios.get('http://localhost:5000/v1/quiz/3', {headers:{
            'Authorization': localStorage.getItem('accessToken')}
            }
        );
        this.questions = next_resp.data.question
        console.log(next_resp.data)

    },
    methods: {

    }
}

</script>