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
			<b-row v-for="(item, index) in education_tab" :key="index" class="my-2">
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
	name: 'EducationComponent',
	props: ['nininfo'],
	components: { UserComboboxVue },
	data() {
		return {
			ninInfo: {},
			dismissSecs: 5,
			dismissCountDown: 0,
			showDismissibleAlert: false,
			education_tab: [
				{
					name: 'User',
					label: 'nin_info',
					type: 'combobox',
					value: null,
				},
				{
					name: 'Highest Education',
					label: 'highest_education',
					type: 'select',
					options: [
						{ value: null, text: 'Enter a option' },
						{ value: 'Primary Education', text: 'Primary Education' },
						{ value: 'Secondary Education', text: 'Secondary Education' },
						{ value: 'Ordinary National Diploma', text: 'OND' },
						{ value: 'Higher National Diploma', text: 'HND' },
						{ value: 'Degree', text: 'Degree' },
						{ value: 'Masters', text: 'Masters' },
						{ value: 'Doctor of Philosophy', text: 'PhD' },
					],
					value: null,
				},
				{
					name: 'Year of Graduation',
					label: 'year_of_graduation',
					type: 'text',
					value: '',
				},
				{
					name: 'Class of Graduation',
					label: 'class_of_graduation',
					type: 'select',
					value: null,
					options: [
						{
							value: null,
							text: 'Choose a Option',
						},
						{
							value: 'First class',
							text: 'First Class',
						},
						{
							value: 'Second class upper',
							text: 'Second Class Upper',
						},
						{
							value: 'Second class lower',
							text: 'Second Class Lower',
						},
						{
							value: 'Third Class',
							text: 'Third Class',
						},
						{
							value: 'Pass',
							text: 'Pass',
						},
					],
				},
				{
					name: 'Name of School',
					label: 'name_of_school',
					type: 'text',
					value: '',
				},
				{
					name: 'Country of Graduation',
					label: 'country_of_graduation',
					type: 'text',
					value: '',
				},
				{
					name: 'Upload Certificate',
					label: 'certificate',
					type: 'file',
					value: null,
				},
				{
					name: 'Upload Transcript',
					label: 'transcript',
					type: 'file',
					value: null,
				},
			],
		};
	},
	mounted() {
		this.getDocument();
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
			const data = this.education_tab.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);

			const formData = new FormData();
			formData.append('certificate.nin_info', this.ninInfo.id);
			formData.append('certificate.path', data.certificate);
			formData.append('certificate.type', 'Certificate');

			formData.append('transcript.nin_info', this.ninInfo.id);
			formData.append('transcript.path', data.transcript);
			formData.append('transcript.type', 'Transcript');

			formData.append('highest_education', data.highest_education);
			formData.append('year_of_graduation', data.year_of_graduation);
			formData.append('class_of_graduation', data.class_of_graduation);
			formData.append('country_of_graduation', data.country_of_graduation);

			await this.axios
				.post(`api/education-document/`, formData, {
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
		async getDocument() {
			const user = JSON.parse(localStorage.getItem('user'));
			await this.axios
				.get(`api/education-document/${user.id}/`)
				.then((result) => {
					console.log(result);
				})
				.catch((err) => {
					console.log(err);
				});
		},
	},
};
</script>
