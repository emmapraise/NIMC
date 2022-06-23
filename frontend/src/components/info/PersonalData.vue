<template>
	<div class="">
		<b-row>
			<b-col
				md="6"
				v-for="(item, index) in personal_data_tab"
				:key="index"
				class="my-1"
			>
				<b-row>
					<b-col md="3">
						<label :for="item.label">{{ item.name }}</label>
					</b-col>
					<b-col md="9">
						<div v-if="item.label === 'marital_status'">
							<b-form-select
								:id="item.label"
								v-model="marital_status_selected"
								required
								:options="marital_status_options"
							></b-form-select>
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
						</div> </b-col
				></b-row>
			</b-col>
		</b-row>
	</div>
</template>
<script>
export default {
	name: 'PersonalDataComponents',
	data() {
		return {
			marital_status_selected: null,
			marital_status_options: [
				{
					value: null,
					text: 'Please select an Option',
				},
				{
					value: 'single',
					text: 'Single',
				},
				{
					value: 'married',
					text: 'Married',
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
					name: 'Marital Status',
					label: 'marital_status',
					type: 'select',
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
