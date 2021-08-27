<template>
  <div>
    <div class="card">
      <div class="card-header">
        <div class="row align-items-center">
          <div class="col">
            <h3 class="mb-0">执行结果</h3>
          </div>
          <div class="col text-right">
            <base-button size="sm" type="primary" @click="clear">
              清空
            </base-button>
          </div>
        </div>
      </div>
      <div class="card-body">
        <div class="row">
          <div class="col">
            <form>
              <textarea
                v-model="log"
                class="form-control"
                id="exampleFormControlTextarea1"
                rows="5"
                placeholder="等待输出(未启用) ..."
                readonly="readonly"
                style="resize: none;"
              ></textarea>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Log",
  components: {},
  props: {},
  data() {
    return {};
  },
  methods: {
    clear() {
      console.log(1);
      this.$store.commit("clearLog");
    },
  },
  computed: {
    log() {
      return this.$store.state.log;
    },
  },
  mounted: function() {
    // let ms = document.getElementById("exampleFormControlTextarea1");
    // setInterval(() => {
    //   ms.scrollTop = ms.scrollHeight;
    //   this.$store.commit("addLog", "测试\n");
    //   console.log(this.$store.state.log);
    // }, 50000);
  },
};
</script>

<style></style>
