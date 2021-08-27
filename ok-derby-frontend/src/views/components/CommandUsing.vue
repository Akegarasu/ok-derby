<template>
  <div>
    <div class="card">
      <div class="card-header">
        <div class="row align-items-center">
          <div class="col">
            <h3 class="mb-0">自定义指令操作（已废弃）</h3>
          </div>
          <div class="col text-right">
            <base-button size="sm" type="primary" @click="gotao()">
              高级编辑器
            </base-button>
          </div>
        </div>
      </div>
      <div class="card-body">
        <div class="row">
          <div class="col">
            <base-input
              placeholder="自定义的运行指令"
              :value="customCommand"
            ></base-input>
          </div>
          <div class="col-3">
            <base-button type="warning">运行</base-button>
            <base-button type="primary" @click="modals.help = true">
              ?
            </base-button>
          </div>
        </div>
      </div>
    </div>
    <modal :show="modals.help" @close="modals.help = false">
      <template v-slot:header>
        <h6 class="modal-title" id="modal-title-default">帮助</h6>
      </template>
      <p>该输入条是启动的指令，若更改请确定你清楚你在做什么</p>
      <template v-slot:footer>
        <base-button type="link" class="ml-auto" @click="modals.help = false"
          >关闭
        </base-button>
      </template>
    </modal>
  </div>
</template>

<script>
export default {
  name: "commandUsing",
  components: {},
  props: {},
  data() {
    return {
      customCommand: "nurting -p afk",
      modals: {
        help: false,
      },
    };
  },
  methods: {
    gotao() {
      this.$notify({
        type: "warning",
        title: "No",
        message: "还没写完呢！",
        timeout: 1500
      });
    },
  },
};
</script>

<style></style>
