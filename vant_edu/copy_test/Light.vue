<template>
  <div>
    <!-- 背景需要设计一个风格 -->
    <van-notice-bar text="xxx在大熊抱点点dasdgasdgvadgfadgfdagsdfg了健康灯"  class="baka"
    :style="{'background-image':`url('${require('../assets/top_bar.png')}')`}" />
    <van-image  height="10rem" fit="cover" :src= "img"/>
    <van-tabs>
      <van-tab v-for="temple in temples" :key="temple.id" :title="temple.name">
        <van-grid  :column-num="3">
          <van-grid-item v-for="light in temple.lights" :key="light.id">
            <van-checkbox icon-size="24px" v-model="light.checked"  @change="selectLight(light)">
              <template #icon="props">
                <!-- <img class="img-icon" :src="props.checked ? activeIcon : lianhuaIcon" /> -->
                <img class="img-icon" 
                :src="props.checked ? activeIcon : inactiveIcon" 
                />
              </template>
            </van-checkbox>
              <van-stepper :default-value="0" :min="0" v-model="light.num"  @change="onChange(light)"/>
              {{light.name}}
          </van-grid-item>
        </van-grid>
      </van-tab>    
    </van-tabs> 
    <van-divider>选择时长</van-divider>
    
        <van-radio-group class="timeSelect" v-model="radio" @change="show = packages[radio].tag || false,durationValue=packages[radio].rate">
            
          <van-row 
            type="flex" 
            justify="space-around"
          >
            <van-col v-for="(type, idx) in packages" 
            :key="idx">
              <van-radio :name="idx" >
                <template #icon>
                  <van-button 
                    size="mini" 
                    :class="idx === radio ? 'checked' : ''"
                  >{{type.name}}</van-button>
                </template>
            </van-radio>
            </van-col>
          </van-row>
        </van-radio-group>
        <van-cell-group>
          <van-field 
          v-if="packages[radio].tag" 
          v-model ="durationValue"
          type="digit" 
          label="自定义天数" placeholder="请输入自定义天数" />
        </van-cell-group>
      <van-divider>选择时长</van-divider>
      <van-row type="flex" class="bottomBug"  justify="space-around">
      <van-col v-for="(type, idx) in packages" 
        :key="idx">
        <van-button 
          size="small" 
          class="bottomStyle"
          :class="idx === radio ? 'checked' : ''"
        >{{type.name}}</van-button>
      </van-col>      
      </van-row>
      <van-submit-bar  class="modified"  :price="sum"  button-type="primary"	 
      button-text="祈福点灯" @submit="onSubmit"/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'


import { Button, Field, Circle, CellGroup,Swipe, SwipeItem,Image,NoticeBar,Panel,
          Tab,Tabs,Grid,GridItem,Icon,Checkbox,CheckboxGroup,Stepper,RadioGroup,Radio,
          Divider,SubmitBar,Toast, Row, Col,DatetimePicker,ActionSheet } from 'vant';
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import {  mapMutations } from 'vuex';

const mock = new MockAdapter(axios);
mock.onGet('/api/ysq_test').reply(200, {
  "code": 0,
  "data": {
    "packages": [
      {
        "id": 0,
        "name": "日供",
        "rate": 1
      },
      {
        "id": 1,
        "name": "\u4e03\u65e5",
        "rate": 7
      },
      {
        "id": 2,
        "name": "\u4e00\u6708",
        "rate": 30
      },
      {
        "id": 3,
        "name": "\u4e03\u4e03\u56db\u5341\u4e5d",
        "rate": 49
      }
    ],
    "temples": [
      {
        "id": 1,
        "lights": [
          {
            "id": 1,
            "name": "\u5065\u5eb7\u706f",
            "price": 0.1
          },
          {
            "id": 2,
            "name": "\u4eb2\u60c5\u706f",
            "price": 0.15
          },
          {
            "id": 3,
            "name": "\u7231\u60c5\u706f",
            "price": 0.22
          },
          {
            "id": 4,
            "name": "\u53cb\u60c5\u706f",
            "price": 0.05
          },
          {
            "id": 5,
            "name": "\u4e8b\u4e1a\u706f",
            "price": 0.25
          },
          {
            "id": 6,
            "name": "\u5b66\u4e1a\u706f",
            "price": 0.12
          },
          {
            "id": 7,
            "name": "\u5e78\u8fd0\u706f",
            "price": 0.23
          },
          {
            "id": 8,
            "name": "\u6843\u82b1\u706f",
            "price": 0.17
          },
          {
            "id": 9,
            "name": "\u968f\u4fbf\u706f",
            "price": 0.32
          }
        ],
        "name": "\u5927\u96c4\u5b9d\u6bbf"
      },
      {
        "id": 2,
        "lights": [],
        "name": "\u5927\u96f7\u97f3\u5bfa"
      },
      {
        "id": 3,
        "name": "\u5c0f\u96f7\u97f3\u5bfa"
      }
    ]
  },
  "msg": ""
});

export default {
  name: 'App',
  components: {
    [Button.name]: Button,
    [Field.name]: Field,
    [Circle.name]: Circle,
    [CellGroup.name]: CellGroup,
    [Swipe.name]:Swipe,
    [SwipeItem.name]:SwipeItem,
    [Image.name]:Image,
    [NoticeBar.name]:NoticeBar,
    [Panel.name]:Panel,
    [Tab.name]:Tab,
    [Tabs.name]:Tabs,
    [Grid.name]:Grid,
    [GridItem.name]:GridItem,
    [Icon.name]:Icon,
    [Checkbox.name]:Checkbox,
    [CheckboxGroup.name]:CheckboxGroup,
    [Stepper.name]:Stepper,
    [RadioGroup.name]:RadioGroup,
    [Radio.name]:Radio,
    [Divider.name]:Divider,
    [SubmitBar.name]:SubmitBar,
    [Toast.name]:Toast,
    [Row.name]: Row,
    [Col.name]: Col,
    [DatetimePicker.name]:DatetimePicker,
    [ActionSheet.name]:ActionSheet,
  },

  data: function() {
    return {
      temples: [],
      packages:[],
      radio: 0,
      btn1Val: 0,
      show:false,
      durationValue : 0,
      checked: true,
      activeIcon: require('../assets/lianhua.png'),
      inactiveIcon: require('../assets/lianhua2.png'),
      img: require("../assets/huihong.jpg"),
      topBar: require("../assets/top_bar.png"),
    }
  },

  computed: {
    btn1Valx10: function() {
      return this.btn1Val * 10;
    },

    
    sum() {
      return this.temples.reduce((a, b) => (
        a + (('lights' in b) ? b.lights.reduce((x, y) => x + (y.num || 0) * ( y.price || 0), 0) : 0)
      ), 0) * 100 * this.durationValue;
    },


  },

  async mounted() {
    let resp = await axios.get('/api/ysq_test');
    this.temples = resp.data.data.temples;
    this.packages = [...resp.data.data.packages, {name: '其他', rate:0,tag: true}];
    this.durationValue = this.packages[0].rate;
    //Toast(JSON.stringify(resp.data.data.temples));

  },

  methods: {
    ...mapMutations(['putSelectlist', 'setDuration']),
    onSubmit() {
      this.putSelectlist(this.temples);
      this.setDuration(this.durationValue);
      /*
      Toast('购买成功');
      */
      this.$router.push('/pay').catch(() => {
        console.log('出错了');
      });

    },
    selectLight(light){
      light.num = +light.checked;
      this.$forceUpdate();//强制更新，否则vant会组织递归调用产生的更新，而产生bug
    },
    onChange(light){
      light.checked = light.num != 0;
    }
  }
}
</script>

<style>

.img-icon {
  height: 20px;
}
 
.baka {
  background-repeat: no-repeat;
  background-size:100% 100%;
  background-position: center;
  background-image: url("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1593264681533&di=e8dd3c48aeea8d2862d58b7bbad35915&imgtype=0&src=http%3A%2F%2Fa3.att.hudong.com%2F14%2F75%2F01300000164186121366756803686.jpg");
}

.van-submit-bar.modified button {
  background-color: rgb(241, 172, 81);
  border-radius: 10px;
}

.van-radio button {
  /* font-size: 1.2em; */
  color: gray;
  background: white;
}

.van-radio button.checked {
  color: white;
  background: rgb(158, 107, 13);
}

/* css选择直接子元素，百度都百度不到 */
div.van-radio > div {
  height: auto !important;
}

.van-tabs__wrap {
  height: 35px;
}

.van-tab{
  padding-bottom: 3px;
  font-weight: bold;
  font-size: 1em;
}
.van-grid-item__content::after {
  border-width: 0px;
}

.van-tabs__line {
  background-color: orange;
}

/* .img-icon {
  filter:  sepia(100%);
} */
.van-stepper__minus{
  border-radius: 999px;
  transform: scale(0.6, 0.6);
  transform-origin: center right;
}
.van-stepper__input[type=text] {
  border-radius: 5px;
  transform: scale(0.8, 0.8);
  color: rgb(158, 107, 13);
}
.van-stepper__plus{
  border-radius: 999px;
  transform: scale(0.6, 0.6);
  transform-origin: center left;
}

.van-hairline {
color: rgb(158, 107, 13);
}
.timeSelect{
}
.setBottom{
  position: fixed;
  bottom:0;
}
.bottomBug{
  padding-bottom: 100%;
}
.bottomStyle{
  color: rgb(233, 231, 227);
  background-color: rgb(158, 107, 13);
  font: bold;
}

</style>
