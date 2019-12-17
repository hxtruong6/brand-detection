<template>
  <div class="Info">
    <div class="Info__wrap" v-if="items.length">
      <div class="Info__display" v-for="(item, i) in items" v-bind:key="item.key">
        <img width="64px" :src="item.brand.logo" />
        <div class="Info__name">
          <span>Name:</span>
          {{item.name}}
        </div>
        <div class="Info__percentCover">
          <span>Percent cover:</span>
          {{percentCover}}
        </div>

        <div class="Info__description">
          <span>Description:</span>
          {{item.brand.description}}
        </div>
        <div class="Info__break" v-show="i!=items.length-1" />
      </div>
    </div>
    <div class="Info__notify" v-else>
      <img width="80%" src="https://i.imgur.com/jtkTPvb.gif?noredirect" />
      <div>No information</div>
      <div style="color: red">{{result.message}}</div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "VideoInfo",
  computed: {
    ...mapState({
      result: state => state.video.result,
      brand: state => state.brand.data
    })
  },
  data() {
    return {
      items: []
    };
  },
  watch: {
    result: function(vals) {
      console.log("xxx 310 result change: ", vals);
      const { name, second, confidence, percentCover } = val;
      this.items = [];
      for (let i = 0; i < vals.length; i++) {
        const { class: name, confidence, percentCover } = vals[i];
        this.items.push({
          key: `img_res_${i}`,
          name,
          confidence: (confidence * 100).toFixed(2),
          brand: this.brand[String(name).toLowerCase()]
        });
      }
    }
  }
};
</script>

<style lang='scss' scoped>
.Info {
  flex: 1.5 1 0;
  flex-flow: column;

  background-color: $third-color-light;
  font-size: 1.8rem;
  display: flex;
  justify-content: center;

  &__wrap {
    overflow: scroll;
  }

  &__display {
    margin: 4px;
    display: flex;
    flex-flow: column nowrap;
    justify-content: space-around;
    span {
      font-weight: bold;

      &:hover {
        font-weight: bolder;
      }
    }
    &__link {
      text-decoration: none;
      text-decoration-color: $third-color;
      cursor: pointer;
      transition: all 0.2s ease;

      &:hover {
        text-decoration: underline;
        font-style: italic;
        transform: translate(-1px) scale(1.05);
      }
    }
  }
  &__percentCover {
    font-size: 2.5rem;
    background-color: #a1dbf8;
    padding: 5px;
    border-radius: 3px;
  }
  &__notify {
    margin: auto;
  }

  &__break {
    height: 3px;
    background-color: $third-color-dark;
  }
}
</style>
