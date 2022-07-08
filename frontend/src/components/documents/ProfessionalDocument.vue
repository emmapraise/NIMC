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
			<b-row
				v-for="(item, index) in professional_tab"
				:key="index"
				class="my-2"
			>
				<b-col sm="3">
					<label :for="item.label">{{ item.name }}</label></b-col
				>
				<b-col sm="9">
					<div v-if="item.type === 'select'">
						<b-form-select
							:id="item.label"
							v-model="item.value"
							required
							:options="item.options"
						></b-form-select>
					</div>
					<div v-else-if="item.type === 'file'">
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
							v-model="item.value"
							required
						></b-form-input></div></b-col
			></b-row>
			<div class="float-right mt-2">
				<b-button variant="success" type="submit">Submit</b-button>
			</div>
		</b-form>
	</div>
</template>
<script>
import UserComboboxVue from '../combobox/UserCombobox.vue';
export default {
	name: 'ProfessionalDocument',
	props: ['nininfo'],
	components: { UserComboboxVue },
	data() {
		return {
			dismissSecs: 5,
			dismissCountDown: 0,
			showDismissibleAlert: false,
			ninInfo: {},
			professional_tab: [
				{
					name: 'User',
					label: 'nin_info',
					type: 'combobox',
					value: null,
				},
				{
					name: 'Name',
					label: 'name',
					type: 'text',
					value: '',
				},
				{
					name: 'Year of Achievement',
					label: 'year',
					type: 'text',
					value: '',
				},
				{
					name: 'Upload proof of certification',
					label: 'proof_of_cert',
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
			const data = this.professional_tab.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);

			const formData = new FormData();
			formData.append('name', data.name);
			formData.append('year_of_achievement', data.year);
			formData.append('document.nin_info', this.ninInfo.id);
			formData.append('document.path', data.proof_of_cert);
			formData.append('document.type', 'Certificate');

			await this.axios
				.post(`api/professional-document/`, formData, {
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
