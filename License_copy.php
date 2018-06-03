<?php
header ( "Content-Type: text/html; charset=utf-8" );
/*解析webpower api*/
$client1 = new SoapClient("http://****.webpower.asia/x/soap-v5.1/wsdl.php");
$client2 = new SoapClient("http://*****.webpower.asia/x/soap-v5.1/wsdl.php");
/*调用createSenderAddress方法*/
$login = array(
    'username'=>'******',
    'password'=>'*****'
);

function copyGroupandRecipient($oldcampaignID,$newcampaignID)
{
	$rg=$client1->getGroups($login,123);
	$oldgroup=$rg->group;
	//创建组并将原平台该组内的联系人上传到新组
	for ($i=15; $i < count($oldgroup); $i++) 
	{ 
	      if ($oldgroup[$i]->is_system==0) 
	      {
	      	  //如果不是系统组，则创建组
	      	  $group=array(
	              'name'=>$oldgroup[$i]->name,
	              'is_test'=>false,
	               'remarks'=>$oldgroup[$i]->remarks
	           );
	          $newgroup=$client2->addGroup($login,22,$group);
	          //并把原有组下的联系人上传到新平台的对应组，需要输入老平台的campaignid和groupid
	          $oldgroupid=$oldgroup[$i]->id;
	          $newgroupid=$newgroup->id;
	          $recipientobj=$client1->getRecipientsFromGroup($login,123,['email','memo','contactpersoncn','address','phone','name','companyname','telephone'],$oldgroupid);
			  $recipients=$recipientobj->recipients;
	          for ($j=0; $j< count($recipients); $j++) { 
		 		$newrecipient=$recipients[$j];
				$client2->addRecipient($login,22,[$newgroupid],$newrecipient,1,1);
			}

	      }
	};

}




?>