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
			<b-row v-for="(item, index) in certificate" :key="index" class="my-2">
				<b-col sm="3">
					<label :for="item.label">{{ item.name }}</label></b-col
				>
				<b-col sm="9">
					<div v-if="item.type === 'file'">
						<b-form-file
							v-model="item.value"
							:state="Boolean(item.value)"
							placeholder="Choose a file or drop it here..."
							drop-placeholder="Drop file here..."
						></b-form-file>
					</div>
					<div v-else-if="item.type === 'combobox'">
						<user-combobox-vue :nininfo="nininfo" @combobox="getCombobox" />
					</div>
					<div v-else>
						<b-form-input
							:id="item.label"
							:type="item.type"
							required
						></b-form-input>
					</div> </b-col
			></b-row>
			<div class="float-right mt-2">
				<b-button variant="success" type="submit">Submit</b-button>
			</div>
		</b-form>
	</div>
</template>
<script>
import UserComboboxVue from '../../combobox/UserCombobox.vue';
export default {
	name: 'CertificateDocument',
	props: ['nininfo'],
	components: { UserComboboxVue },
	data() {
		return {
			dismissSecs: 5,
			dismissCountDown: 0,
			showDismissibleAlert: false,
			ninInfo: {},
			certificate: [
				{
					name: 'User',
					label: 'nin_info',
					type: 'combobox',
					value: '',
				},
				{
					name: 'Upload Certificate',
					label: 'upload_cert',
					type: 'file',
					value: null,
				},
				{
					name: 'Upload Transcript',
					label: 'upload_transcript',
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
		getCombobox(value) {
			this.ninInfo = value;
		},
		async onSubmit() {
			const data = this.certificate.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			console.log(this.ninInfo);
			const formData = new FormData();
			formData.append('certificate.nin_info', this.ninInfo.id);
			formData.append('certificate.path', data.upload_cert);
			formData.append('certificate.type', 'Certificate');

			formData.append('transcript.nin_info', this.ninInfo.id);
			formData.append('transcript.path', data.upload_transcript);
			formData.append('transcript.type', 'Transcript');

			await this.axios
				.post(`api/certificate/`, formData, {
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
	},
};
</script>
