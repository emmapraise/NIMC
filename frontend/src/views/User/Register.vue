<template>
	<div class="container">
		<b-tabs content-class="mt-3 w-50 mx-auto" justified>
			<b-tab title="Name" active>
				<b-row v-for="(item, index) in name_tab" :key="index" class="my-2">
					<b-col sm="3">
						<label :for="item.label">{{ item.name }}</label></b-col
					>
					<b-col sm="9">
						<b-form-input
							:id="item.label"
							:type="item.type"
						></b-form-input></b-col></b-row
			></b-tab>

			<b-tab title="Personal Data">
				<b-row
					v-for="(item, index) in personal_data_tab"
					:key="index"
					class="my-2"
				>
					<b-col sm="3">
						<label :for="item.label">{{ item.name }}</label>
					</b-col>
					<b-col sm="9">
						<div v-if="item.label === 'marital_status'">
							<b-form-select
								:id="item.label"
								v-model="marital_status_selected"
								:options="marital_status_options"
							></b-form-select>
						</div>
						<div v-else-if="item.label === 'gender'">
							<b-form-radio-group
								:id="item.label"
								v-model="gender_selected"
								:options="gender_options"
							></b-form-radio-group>
						</div>
						<div v-else-if="item.label === 'home_address'">
							<b-form-textarea
								:id="item.label"
								max-rows="6"
								rows="3"
								v-model="item.value"
							>
							</b-form-textarea>
						</div>
						<div v-else>
							<b-form-input
								:id="item.label"
								:type="item.type"
								v-model="item.value"
							></b-form-input>
						</div>
					</b-col>
				</b-row>
				<b-button @click="done">Submit</b-button>
			</b-tab>
			<b-tab title="Medical Details">
				<b-row class="my-2" v-for="(item, index) in medical_tab" :key="index">
					<b-col sm="3">
						<label :for="item.label">{{ item.name }} </label>
					</b-col>
					<b-col sm="9">
						<div v-if="item.type === 'select'">
							<b-form-select
								:id="item.label"
								v-model="item.value"
								:options="item.options"
							></b-form-select>
						</div>
					</b-col>
				</b-row>
			</b-tab>
			<b-tab title="Kinship Details">
				<b-row class="my-2" v-for="(item, index) in kinship_tab" :key="index">
					<b-col sm="3">
						<label :for="item.label"> {{ item.name }}</label>
					</b-col>
					<b-col sm="9">
						<div v-if="item.type === 'textarea'">
							<b-form-textarea
								:id="item.label"
								max-rows="6"
								rows="3"
								v-model="item.value"
							>
							</b-form-textarea>
						</div>
						<div v-else>
							<b-form-input
								:id="item.label"
								:type="item.type"
								v-model="item.value"
							></b-form-input>
						</div>
					</b-col>
				</b-row>
			</b-tab>
		</b-tabs>
	</div>
</template>
<script>
export default {
	name: 'RegisterView',
	data() {
		return {
			gender_selected: null,
			gender_options: [
				{ value: 'M', text: 'Male' },
				{ value: 'F', text: 'Female' },
			],
			marital_status_selected: null,
			marital_status_options: [
				{
					value: null,
					text: 'Please select an Option',
				},
				{
					value: 'married',
					text: 'Married',
				},
				{
					value: 'single',
					text: 'Single',
				},
				{
					value: 'divorced',
					text: 'Divorced',
				},
			],
			name_tab: [
				{
					name: 'Surname',
					label: 'surname',
					type: 'text',
				},
				{
					name: 'First Name',
					label: 'last_name',
					type: 'text',
				},
				{
					name: 'Middle Name',
					label: 'middle_name',
					type: 'text',
				},
			],
			personal_data_tab: [
				{
					name: 'Date of Birth',
					label: 'dob',
					type: 'date',
					value: '',
				},
				{
					name: 'Gender',
					label: 'gender',
					type: 'radio',
					value: '',
				},
				{
					name: 'Marital Status',
					label: 'marital_status',
					type: 'select',
					value: '',
				},
				{
					name: 'Email Address',
					label: 'email',
					type: 'email',
					value: '',
				},
				{
					name: 'Phone Number',
					label: 'phone_number',
					type: 'tel',
					value: '',
				},
				{
					name: 'Home Address',
					label: 'home_address',
					type: 'textarea',
					value: '',
				},
			],
			medical_tab: [
				{
					name: 'Blood Group',
					label: 'blood_group',
					value: null,
					options: [
						{ value: null, text: 'Select a Option' },
						{ value: 'A', text: 'A' },
						{ value: 'B', text: 'B' },
						{ value: 'AB', text: 'AB' },
						{ value: 'O', text: 'O' },
					],
					type: 'select',
				},
				{
					name: 'Genotype',
					label: 'genotype',
					value: null,
					type: 'select',
					options: [
						{ value: null, text: 'Select a Option' },
						{ value: 'AA', text: 'AA' },
						{ value: 'AS', text: 'AS' },
						{ value: 'AC', text: 'AC' },
						{ value: 'SS', text: 'SS' },
					],
				},
			],
			kinship_tab: [
				{
					name: 'Next of Kin',
					label: 'next_of_kin',
					type: 'text',
					value: '',
				},
				{
					name: 'Next of Kin Email',
					label: 'next_of_kin_email',
					type: 'email',
					value: '',
				},
				{
					name: 'Next of Kin Phone Number',
					label: 'next_of_kin_phone',
					type: 'tel',
					value: '',
				},
				{
					name: 'Next of Kin Address',
					label: 'next_of_kin_address',
					type: 'textarea',
					value: '',
				},
			],
		};
	},
	mounted() {
		console.log('object');
		this.done();
	},
	methods: {
		done() {
			console.log(this.personal_data_tab);
		},
	},
};
</script>
