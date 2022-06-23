<template>
	<div class="">
		<b-row>
			<b-col md="6" v-for="(item, index) in name_tab" :key="index" class="my-1">
				<b-row>
					<b-col md="3">
						<label :for="item.label">{{ item.name }}</label></b-col
					>
					<b-col md="9">
						<div v-if="item.type === 'radio'">
							<b-form-radio-group
								:id="item.label"
								v-model="item.value"
								required
								:options="item.options"
							></b-form-radio-group>
						</div>
						<div v-else>
							<b-form-input
								:id="item.label"
								:type="item.type"
								required
							></b-form-input>
						</div> </b-col></b-row></b-col
		></b-row>
	</div>
</template>
<script>
export default {
	name: 'NameComponet',
	data() {
		return {
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
				{
					name: 'Gender',
					label: 'gender',
					type: 'radio',
					value: null,
					options: [
						{ value: 'M', text: 'Male' },
						{ value: 'F', text: 'Female' },
					],
				},
				{
					name: 'Email',
					label: 'email',
					type: 'email',
					value: '',
				},
				{
					name: 'Phone',
					label: 'phone_number',
					type: 'tel',
					value: '',
				},
			],
		};
	},
};
</script>
