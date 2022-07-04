<template>
	<div>
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
					<user-combobox-vue :citizens="citizens" />
				</div>
				<div v-else>
					<b-form-input
						:id="item.label"
						:type="item.type"
						required
					></b-form-input></div></b-col
		></b-row>
		<div class="float-right mt-2">
			<b-button variant="success">Submit</b-button>
		</div>
	</div>
</template>
<script>
import UserComboboxVue from '../combobox/UserCombobox.vue';
export default {
	name: 'EducationComponent',
	props: ['citizens'],
	components: { UserComboboxVue },
	data() {
		return {
			result: '',
			user: {},
			education_tab: [
				{
					name: 'User',
					label: 'citizen',
					type: 'combobox',
					value: '',
				},
				{
					name: 'Highest Education',
					label: 'education_type',
					type: 'select',
					options: [
						{ value: null, text: 'Enter a option' },
						{ value: 'Primary', text: 'Primary Education' },
						{ value: 'Secondary', text: 'Secondary Education' },
						{ value: 'Degree', text: 'Degree' },
						{ value: 'OND', text: 'OND' },
						{ value: 'HND', text: 'HND' },
						{ value: 'Masters', text: 'Masters' },
						{ value: 'PhD', text: 'PhD' },
					],
					value: null,
				},
				{
					name: 'Year of Graduation',
					label: 'year_of_grad',
					type: 'text',
					value: '',
				},
				{
					name: 'Class of Graduation',
					label: 'class_of_grad',
					type: 'select',
					value: null,
					options: [
						{
							value: null,
							text: 'Choose a Option',
						},
						{
							value: 'First',
							text: 'First Class',
						},
						{
							value: 'Second Upper',
							text: 'Second Class Upper',
						},
						{
							value: 'Second Lower',
							text: 'Second Class Lower',
						},
						{
							value: 'Third',
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
					label: 'country_of_grad',
					type: 'text',
					value: '',
				},
				{
					name: 'Upload Certificate',
					label: 'upload_certificate',
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
		comboboxEvent() {
			const nin = this.result.split(' ')[0];
			this.user = this.citizens.find((o) => o.user.nin === nin);
		},
	},
};
</script>
