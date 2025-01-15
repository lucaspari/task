<template>
  <v-dialog
    v-model="localDialog"
    max-width="500px"
  >
    <v-card>
      <v-card-title class="text-h5">
        Edit User
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col
              cols="6"
              md="6"
              sm="6"
            >
              <v-text-field
                v-model="editedUser.username"
                label="username"
              />
            </v-col>
            <v-col
              cols="6"
              md="6"
              sm="6"
            >
              <v-checkbox
                v-model="editedUser.active"
                label="active"
              />
            </v-col>
          </v-row>
          <v-row
            align="center"
            justify="center"
          >
            <v-col
              cols="12"
              align="center"
              md="6"
              sm="6"
            >
              <v-text-field
                v-model="editedUser.preferences"
                label="timezone"
              />
            </v-col>
          </v-row>
          <v-card-actions>
            <v-spacer />
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="close"
            >
              Cancel
            </v-btn>
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="save"
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-container>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
export default {
  name : "EditDialog",
  props:{
    dialog: {
      type: Boolean,
      required: true
    },
    user:{
      type: Object,
      required: true
    }
  },
  emits: ['update:dialog', 'update:save'],
  data() {
    return {
      localDialog: false,
      editedUser: {
        username: '',
        active: false,
        preferences: ''
      }
    };
  },
  watch: {
    dialog(val) {
      this.localDialog = val;
    },
    localDialog(val) {
      this.$emit('update:dialog', val);
    },
    user(val){
      this.editedUser = val;
    }
  },
  methods: {
    close() {
      this.$emit('update:dialog', false);
    },
    save(){
    this.$emit('update:save', this.editedUser);
    this.close();
    }
  }
};
</script>

<style scoped>
</style>
