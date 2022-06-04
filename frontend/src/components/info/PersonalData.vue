<template>
	<div class="container">
		<b-row v-for="(item, index) in personal_data_tab" :key="index" class="my-2">
			<b-col sm="3">
				<label :for="item.label">{{ item.name }}</label>
			</b-col>
			<b-col sm="9">
				<div v-if="item.label === 'marital_status'">
					<b-form-select
						:id="item.label"
						v-model="marital_status_selected"
						required
						:options="marital_status_options"
					></b-form-select>
				</div>
				<div v-else-if="item.label === 'gender'">
					<b-form-radio-group
						:id="item.label"
						v-model="gender_selected"
						required
						:options="gender_options"
					></b-form-radio-group>
				</div>
				<div v-else-if="item.label === 'home_address'">
					<b-form-textarea
						:id="item.label"
						max-rows="6"
						required
						rows="3"
						v-model="item.value"
					>
					</b-form-textarea>
				</div>
				<div v-else>
					<b-form-input
						:id="item.label"
						required
						:type="item.type"
						v-model="item.value"
					></b-form-input>
				</div>
			</b-col>
		</b-row>
	</div>
</template>
<script>
export default {
	name: 'PersonalDataComponents',
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
		};
	},
};
</script>
