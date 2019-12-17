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
          {{item.cover}}%
        </div>

        <div class="Info__freq">
          <span>Frequently:</span>
          {{item.freq}}%
        </div>

        <el-collapse class="Info__description" style="color: red">
          <el-collapse-item title="Description">{{item.brand.description}}</el-collapse-item>
        </el-collapse>

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
      if (!vals.ok) return;
      const { data } = vals;
      console.log("xxx 311 data: ", data);

      this.items = [];
      for (let i = 0; i < data.length; i++) {
        const { name, cover, freq } = data[i];
        this.items.push({
          key: `vi_res_${i}`,
          name,
          freq,
          cover,
          brand: this.brand[String(name).toLowerCase()]
        });
      }
      console.log("xxx 313 result : ", this.items);
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
    height: 100%;
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

  &__description {
    & > div {
      background-color: $third-color-light;
      font-size: 2rem;
    }
  }

  &__percentCover {
    font-size: 2.5rem;
    background-color: #a1dbf8;
    padding: 4px;
    margin: 2px 0;
    border-radius: 3px;
  }

  &__freq {
    font-size: 2.5rem;
    background-color: #f7ea72;
    padding: 4px;
    margin: 2px 0;
    border-radius: 3px;
  }

  &__notify {
    margin: auto;
    text-align: center;
    font-size: 2rem;
  }

  &__break {
    height: 3px;
    background-color: $third-color-dark;
  }
}
</style>
