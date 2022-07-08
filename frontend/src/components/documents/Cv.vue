<template>
	<div>
		<b-alert
			:show="dismissCountDown"
			dismissible
			variant="success"
			@dismissed="dismissCountDown = 0"
			@dismiss-count-down="countDownChanged"
		>
			<p>Document Uploaded Successfully</p>
		</b-alert>

		<b-form @submit.prevent="onSubmit">
			<b-row v-for="(item, index) in cv_tab" :key="index" class="my-2">
				<b-col sm="3">
					<label :for="item.label">{{ item.name }}</label>
				</b-col>
				<b-col sm="9">
					<div v-if="item.type === 'combobox'">
						<user-combobox-vue :nininfo="nininfo" @combobox="getCombobox" />
					</div>
					<div v-else>
						<b-form-file
							v-model="file"
							:state="Boolean(file)"
							placeholder="Choose a file or drop it here..."
							drop-placeholder="Drop file here..."
						></b-form-file>
					</div>
				</b-col>
			</b-row>
			<div class="float-right mt-3">
				<b-button variant="success" type="submit">Submit</b-button>
			</div>
		</b-form>
	</div>
</template>
<script>
import UserComboboxVue from '../combobox/UserCombobox.vue';
export default {
	name: 'CVComponent',
	components: { UserComboboxVue },
	props: ['nininfo'],
	data() {
		return {
			ninInfo: {},
			file: null,
			dismissSecs: 5,
			dismissCountDown: 0,
			showDismissibleAlert: false,
			cv_tab: [
				{
					name: 'User',
					label: 'citizen',
					type: 'combobox',
					value: null,
				},
				{
					name: 'Upload CV',
					label: 'upload_cv',
					type: 'file',
					value: null,
				},
			],
		};
	},
	methods: {
		countDownChanged(dismissCountDown) {
			this.dismissCountDown = dismissCountDown;
		},
		showAlert() {
			this.dismissCountDown = this.dismissSecs;
		},
		async onSubmit() {
			const formData = new FormData();
			formData.append('nin_info', this.ninInfo.id);
			formData.append('type', 'Curriculum Vitae');
			formData.append('path', this.file);

			await this.axios
				.post(`api/document/`, formData, {
					headers: {
						'content-type': 'multipart/form-data',
					},
				})
				.then(() => {
					this.showAlert();
					this.$router.go();
				})
				.catch(() => {});
		},
		getCombobox(value) {
			this.ninInfo = value;
		},
	},
};
</script>
