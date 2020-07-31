<template>
  <div >
    <!-- 背景需要设计一个风格 -->
    <van-notice-bar text=输入文字   />
    <van-steps :active="active" active-icon="success" active-color="#38f">
    <van-step>选择点灯</van-step>
    <van-step>祈愿并支付</van-step>
    <van-step>祈愿完成</van-step>
    </van-steps>    
    <van-cell-group>
        <van-field label="供灯金额" :value="money.toFixed(2)"  readonly />
        <van-field label="姓名" placeholder="点击输入姓名" />
        <van-field label="电话" type="tel" placeholder="点击输入号码" />
        <van-field label="祈愿" placeholder="点击输入祈愿愿望" />
    </van-cell-group>
    <van-button color="#7232dd"  block  @click="prayPay()">祈愿支付</van-button>
  </div>
</template>

<script>
import { Button, Field, Circle, CellGroup,Swipe, SwipeItem,Image,NoticeBar,Panel,
          Icon,Checkbox,CheckboxGroup,Stepper,RadioGroup,Radio,
          Divider,SubmitBar,Toast, Row, Col ,Step,Steps} from 'vant';
import { mapGetters, mapState } from 'vuex';
// import axios from 'axios';

import wx from 'weixin-js-sdk';


export default {
  name: 'Pay',
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
    [Step.name]:Step,
    [Steps.name]:Steps,
  },
  data:function(){
      return{
          active:1,
          testdata:[],
      }
  },
  computed: {
    ...mapGetters(['money']),
    ...mapState(
      ['selectList']
    ),

  },


  methods:{

      prayPay(){
        // store.getters.testlist;
        console.log(this.selectList);

        let res = {
          payList: this.selectList.map(({id: templeId, lights}) => ({
            templeId,
            lights: (lights || []).filter(({num}) => num > 0).map(({id, num}) => ({
              id,
              num,
            }),
          )})).filter(({lights}) => lights.length > 0),
          duration: 233,
        };

        console.log(res);

      
        // for(let item of this.$store.state.selectList){
        //   console.log(item.id,(item.lights || []).filter(ele=> ele.num>0))
        // }

        // console.log(this.$store.state.selectList[0].lights.filter(ele => ele.num>0));
      },
      getWxJdk(){


        wx.config({
        debug: true, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
        appId: 'wxee0adc393f17bce7', // 必填，公众号的唯一标识
        timestamp: 12, // 必填，生成签名的时间戳
        nonceStr: '67eba5b428d3e2ea59b622a152dce57e', // 必填，生成签名的随机串
        signature: '',// 必填，签名
        jsApiList: [] // 必填，需要使用的JS接口列表
      });

      }
  },

  }
</script>
